from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel


class VideoWidget(QLabel):

    def __init__(self):

        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.setText("En attente du flux vidéo...")

        self.setMinimumSize(960, 540)

    def update_frame(self, image):

        pix = QPixmap.fromImage(image)

        self.setPixmap(
            pix.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )