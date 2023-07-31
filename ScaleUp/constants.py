import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEO_CODECS_LIST = {
    "H264": "libx264",
    "HEVC": "hevc",
    "MPEG4": "mpeg4",
    "Theora": "libtheora",
    "VP8": "libvpx",
    "VP9": "libvpx-vp9",
    "FLV": "flv"
}
AUDIO_CODECS_LIST = {
    "AAC": "aac",
    "Vorbis": "libvorbis",
    "Opus": "libopus",
    "MP3": "libmp3lame"
}

MODELS_LIST = {
    "realesrgan-x4plus": 4,
    "RealESRGAN_General_x4_v3": 4,
    "realesr-animevideov3-x2": 2,
    "realesr-animevideov3-x3": 3,
    "realesr-animevideov3-x4": 4,
    "realesr-animevideov3-x4plus": 4,
    "realesrgan-x4plus-anime": 4
}
