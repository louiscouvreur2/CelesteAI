import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow

from agent.celeste_agent import CelesteAgent

class Application:

    def __init__(self, mode="record"):

        self.agent = CelesteAgent()

        self.mode = mode

        self.qt = QApplication(sys.argv)

        self.window = MainWindow()

    def run(self):

        if self.mode == "record":

            print("=== RECORD MODE ===")

        elif self.mode == "play":

            self.agent.run()

            return 0

        elif self.mode == "train":

            print("=== TRAIN MODE ===")

        else:

            raise ValueError(f"Mode inconnu : {self.mode}")

        self.window.show()

        return self.qt.exec()