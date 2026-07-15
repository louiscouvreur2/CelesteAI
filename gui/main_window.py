from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from config.settings import *

from gui.status_panel import StatusPanel

from gui.video_widget import VideoWidget
from core.signals import AppSignals
from capture.capture_thread import CaptureThread

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

        self.video = VideoWidget()

        self.video.setMinimumSize(960, 540)

        self.video.setStyleSheet("""
            background:black;
            color:white;
            border:2px solid gray;
        """)

        layout.addWidget(self.video)

        self.signals = AppSignals()

        self.signals.frame_ready.connect(
            self.video.update_frame
        )

        self.thread = CaptureThread(self.signals)

        self.thread.start()

        def closeEvent(self, event):

            self.thread.stop()

            self.thread.wait()

            event.accept()
