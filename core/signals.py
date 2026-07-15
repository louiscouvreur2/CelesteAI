from PySide6.QtCore import QObject
from PySide6.QtCore import Signal


class AppSignals(QObject):

    frame_ready = Signal(object)

    fps_updated = Signal(float)