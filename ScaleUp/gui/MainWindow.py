from PySide6.QtWidgets import QWidget, QSpinBox, QMessageBox
from ScaleUp.gui.ui_MainWindow import Ui_MainWindow
from ScaleUp.gui.AboutDialog import AboutDialog
from ScaleUp.gui.ProgressDialog import ProgressDialog
from ScaleUp.constants import VIDEO_CODECS_LIST, AUDIO_CODECS_LIST, MODELS_LIST
from ScaleUp.core.Upscaler import Upscaler


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self._SAME_RESOLUTION = self.tr("Any/Keep the resolution same")
        self._NO_SOUND = self.tr("No sound")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.videoCodecInput.addItems(VIDEO_CODECS_LIST.keys())

        self.ui.audioCodecInput.addItems(list(AUDIO_CODECS_LIST.keys()) + [self._NO_SOUND])

        self.ui.upscalerModelInput.addItems([self._SAME_RESOLUTION] + list(MODELS_LIST.keys()))
        self.ui.upscalerModelInput.currentTextChanged.connect(self._set_scale)

        self.ui.scaleInput = self.findChild(QSpinBox, "scaleInput")

        self.ui.aboutButton.clicked.connect(self._show_about)
        self.ui.startButton.clicked.connect(self._start_upscaling)

    def _set_scale(self, event):
        model_name = self.ui.upscalerModelInput.currentText()

        if model_name == self._SAME_RESOLUTION:
            self.ui.scaleInput.setValue(0)
        else:
            self.ui.scaleInput.setValue(MODELS_LIST[model_name])

    def _show_about(self, event):
        AboutDialog().exec()

    def _start_upscaling(self, event):
        source_file = self.ui.sourceFileSelection.getSelectedFile()
        dest_file = self.ui.destinationFileSelection.getSelectedFile()

        if not (source_file and dest_file):
            QMessageBox.critical(
                self,
                self.tr("Error"),
                self.tr("You need to select source and destination files to continue.")
            )

            self.setDisabled(False)

            return

        self.setDisabled(True)

        model_name = self.ui.upscalerModelInput.currentText()
        audio_codec = self.ui.audioCodecInput.currentText()

        ProgressDialog(
            self.ui.sourceFileSelection.getSelectedFile(),
            self.ui.destinationFileSelection.getSelectedFile(),
            VIDEO_CODECS_LIST[self.ui.videoCodecInput.currentText()],
            AUDIO_CODECS_LIST[self.ui.audioCodecInput.currentText()] if audio_codec != self._NO_SOUND else None,
            Upscaler(model_name, self.ui.scaleInput.value()) if model_name != self._SAME_RESOLUTION else None
        )

        self.setDisabled(False)
