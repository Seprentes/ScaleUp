from PySide6.QtWidgets import QMessageBox


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.tr("About"))

        self.setText(self.tr("""
<h3>About ScaleUp</h3>
<p>Copyright (C) 2023 Özgür Ateş Fırat</p>
<p>ScaleUp, is a software that uses the RealESRGAN artificial intelligence to enhance the resolution of videos, making them higher quality.</p>
<p>Some technologies used for making ScaleUp:
<ul>
    <li><a href="https://doc.qt.io/qtforpython-6/index.html">PySide6<a/></li>
    <li><a href="https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan">Real-ESRGAN-ncnn-vulkan</a></li>
    <li><a href="https://pyav.org/">PyAV</a></li>
    <li><a href="https://github.com/Seprentes/python-realesrgan-ncnn-vulkan">python-realesrgan-ncnn-vulkan</a></li>
</ul>
"""))

        self.show()
