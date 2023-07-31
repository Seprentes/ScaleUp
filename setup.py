#!/usr/bin/env python3

import os
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py


class BuildCommand(build_py):
    def run(self):
        self._process_ui()
        self._process_translations()

        super().run()

    def _process_ui(self):
        targets_and_dests = {
            os.path.join("ScaleUp", "gui", "MainWindow.ui"): os.path.join("ScaleUp", "gui", "ui_MainWindow.py"),
            os.path.join("ScaleUp", "gui", "FileSelection", "FileSelection.ui"): os.path.join("ScaleUp", "gui", "FileSelection", "ui_FileSelection.py")
        }

        for target, destination in targets_and_dests.items():
            subprocess.run(["pyside6-uic", target, "-o", destination])

    def _process_translations(self):
        locales_path = os.path.join("ScaleUp", "i18n")

        for file_name in os.listdir(locales_path):
            if not file_name.endswith(".ts"):
                continue

            file_path = os.path.join(locales_path, file_name)
            destination_path = os.path.splitext(file_path)[0] + ".qm"

            subprocess.run(["pyside6-lrelease", file_path, "-qm", destination_path])


setup(
    name="ScaleUp",
    version="1.0.1",
    description="Real-ESRGAN based video upscaler",
    author="Özgür Ateş Fırat",
    author_email="ozgurafirat@proton.me",
    url="https://github.com/Seprentes/ScaleUp",
    packages=["ScaleUp", "ScaleUp.core", "ScaleUp.gui", "ScaleUp.gui.FileSelection"],
    package_data={
        "ScaleUp": [
            "icon.png",
            "i18n/*.qm",
            "models/*"
        ]
    },
    cmdclass={"build_py": BuildCommand}
)
