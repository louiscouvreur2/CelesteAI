from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class StatusPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.game = QLabel("🎮 Jeu : Non détecté")

        self.capture = QLabel("📹 Capture : Arrêtée")

        self.model = QLabel("🧠 Modèle : Aucun")

        self.fps = QLabel("⚡ FPS : 0")

        layout.addWidget(self.game)

        layout.addWidget(self.capture)

        layout.addWidget(self.model)

        layout.addWidget(self.fps)

        layout.addStretch()