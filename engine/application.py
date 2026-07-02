import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow


class Application:

    def __init__(self):

        self.qt = QApplication(sys.argv)

        self.window = MainWindow()

    def run(self):

        self.window.show()

        return self.qt.exec()