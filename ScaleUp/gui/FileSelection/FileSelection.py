from PySide6.QtWidgets import QFrame, QFileDialog
from ScaleUp.gui.FileSelection.ui_FileSelection import Ui_FileSelection


class FileSelection(QFrame):
    _existing_file = False

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_FileSelection()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self._file_selector)

    def _file_selector(self, event):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile if self._existing_file else QFileDialog.AnyFile)

        file_path = file_dialog.getOpenFileName()[0]

        if file_path:
            self.ui.lineEdit.setText(file_path)

    def getSelectedFile(self):
        return self.ui.lineEdit.text()

    def getExistingFile(self):
        return self._existing_file

    def setExistingFile(self, value):
        self._existing_file = value
