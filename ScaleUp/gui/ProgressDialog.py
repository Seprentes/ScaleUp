from PySide6.QtWidgets import QApplication, QProgressDialog, QMessageBox
from ScaleUp.core.VideoConventer import VideoConventer


class ProgressDialog(QProgressDialog):
    _range_determined = False

    def __init__(self, src, dest, dest_codec, dest_audio_codec, upscaler):
        super().__init__()

        self._PROGRESS_INFO = self.tr("Completed: {}/{}")

        self.setWindowTitle(self.tr("Please Wait"))
        self.setLabelText(self.tr("Processing..."))
        self.setCancelButton(None)
        self.setAutoClose(True)
        self.show()

        self.setValue(0)
        QApplication.processEvents()

        try:
            VideoConventer(
                self._update_status,
                src,
                dest,
                dest_codec,
                dest_audio_codec,
                upscaler
            )
        except Exception as e:
            error = QMessageBox(QMessageBox.Icon.Critical, self.tr("Error"), self.tr("Error while processing."))
            error.setDetailedText(str(e))

            error.exec()

    def closeEvent(self, event):
        event.ignore()

    def _update_status(self, status):
        print(status[0], status[1])

        if not self._range_determined:
            self.setRange(0, status[1])

        self.setLabelText(self._PROGRESS_INFO.format(status[0], status[1]))
        self.setValue(status[0])

        QApplication.processEvents()
