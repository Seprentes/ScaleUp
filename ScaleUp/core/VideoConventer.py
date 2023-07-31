import av


class VideoConventer:
    def __init__(self, update_status, src, dest, dest_codec, dest_audio_codec, upscaler):
        self._input_container = av.open(src)

        self._input_video_stream = self._input_container.streams.video[0]
        self._input_audio_stream = self._input_container.streams.audio[0] if dest_audio_codec and self._input_container.streams.audio else None

        self._upscaler = upscaler
        if upscaler:
            self.dest_width, self.dest_height = (
                self._input_video_stream.width * upscaler.scale,
                self._input_video_stream.height * upscaler.scale
            )
        else:
            self.dest_width, self.dest_height = (
                self._input_video_stream.width,
                self._input_video_stream.height
            )

        self._output_container = av.open(dest, mode="w")

        self._output_video_stream = self._output_container.add_stream(
            dest_codec,
            rate=self._input_video_stream.average_rate
        )
        self._output_video_stream.width = self.dest_width
        self._output_video_stream.height = self.dest_height
        self._output_video_stream.bit_rate = self._input_video_stream.bit_rate

        self._output_audio_stream = self._output_container.add_stream(
            dest_audio_codec,
            rate=self._input_audio_stream.average_rate
        ) if self._input_audio_stream else None

        self._update_status = update_status

        self._convert_video()

    def _convert_video(self):
        current_frame = 0
        for packet in self._input_container.demux([self._input_video_stream, self._input_audio_stream]) if self._input_audio_stream else self._input_container.demux([self._input_video_stream]):
            if packet.stream == self._input_video_stream:
                for frame in packet.decode():
                    current_frame += 1

                    frame = frame.to_rgb()

                    if self._upscaler:
                        upscaled_img = self._upscaler.process(
                            self._input_video_stream.width,
                            self._input_video_stream.height,
                            frame.planes[0].to_bytes()
                        )

                        frame = av.VideoFrame(
                            width=self.dest_width,
                            height=self.dest_height,
                            format="rgb24"
                        )

                        frame.planes[0].update(upscaled_img)

                    self._output_container.mux(self._output_video_stream.encode(frame))

                    self._update_status((current_frame, self._input_video_stream.frames))
            elif packet.stream == self._input_audio_stream:
                decoded_packet = packet.decode()

                if decoded_packet == []:
                    continue

                self._output_container.mux(self._output_audio_stream.encode(decoded_packet[0]))

        for packet in self._output_video_stream.encode():
            self._output_container.mux(packet)

        if self._output_audio_stream:
            for packet in self._output_audio_stream.encode():
                self._output_container.mux(packet)

        self._input_container.close()
        self._output_container.close()
