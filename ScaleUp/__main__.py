import os
import sys
from PySide6.QtCore import QLocale, QTranslator
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication
from ScaleUp.gui.MainWindow import MainWindow
from ScaleUp.constants import ROOT_DIR


def main():
    app = QApplication(sys.argv)

    translator = QTranslator()
    translator.load(os.path.join(ROOT_DIR, "i18n", QLocale.system().name()))

    app.installTranslator(translator)
    app.setWindowIcon(QPixmap(os.path.join(ROOT_DIR, "icon.png")))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
