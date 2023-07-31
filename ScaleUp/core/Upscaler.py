import os
from realesrgan_ncnn_vulkan import RealESRGAN
from ScaleUp.constants import ROOT_DIR


class Upscaler:
    def __init__(self, model, scale):
        parampath = os.path.join(ROOT_DIR, "models", f"{model}.param")
        modelpath = os.path.join(ROOT_DIR, "models", f"{model}.bin")

        self.scale = scale

        self.upscaler = RealESRGAN()
        self.upscaler.load(parampath, modelpath)
        self.upscaler.scale = self.scale

    def process(self, width, height, image_data):
        return self.upscaler.process(width, height, image_data, 3)
