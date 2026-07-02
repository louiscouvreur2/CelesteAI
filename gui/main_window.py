from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from config.settings import *

from gui.status_panel import StatusPanel


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        root = QWidget()

        self.setCentralWidget(root)

        layout = QHBoxLayout(root)

        left = QVBoxLayout()

        left.addWidget(StatusPanel())

        left.addWidget(QPushButton("Vision"))

        left.addWidget(QPushButton("Recorder"))

        left.addWidget(QPushButton("Train"))

        left.addWidget(QPushButton("Play"))

        left.addStretch()

        layout.addLayout(left)

        self.video = QLabel("Video Stream")

        self.video.setMinimumSize(960, 540)

        self.video.setStyleSheet("""
            background:black;
            color:white;
            border:2px solid gray;
        """)

        layout.addWidget(self.video)