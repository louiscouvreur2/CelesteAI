from __future__ import annotations

import cv2

from capture import frame
from capture.capture_manager import CaptureManager
from capture.window import find_celeste_window

from vision.pipeline import VisionPipeline

from capture.debug_window import DebugWindow

class GameManager:

    def __init__(self):

        self.debug = DebugWindow()

        self.window = find_celeste_window()

        if self.window is None:
            raise RuntimeError("Celeste non trouvé.")

        self.capture = CaptureManager()

        self.pipeline = VisionPipeline()

        self.window = find_celeste_window()

        if self.window is None:
            raise RuntimeError("Impossible de trouver Celeste.")

    def run(self):

        self.capture.start()

        try:

            while True:

                frame = self.capture.get_frame()

                if frame is None:
                    continue

                processed = self.pipeline.process(frame.image)

                if not self.debug.show(processed):
                    break

        finally:

            self.capture.stop()

            cv2.destroyAllWindows()

            self.debug.close()