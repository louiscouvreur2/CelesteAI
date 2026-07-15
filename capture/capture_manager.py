from __future__ import annotations

import time

import dxcam

from capture.frame import Frame


class CaptureManager:
    """
    Capture tout l'écran avec DXCam.
    """

    def __init__(self):

        self.camera = dxcam.create()

        self.frame_id = 0

    def start(self):

        try:

            self.camera.start(target_fps=60)

        except RuntimeError:

            pass
 
    def stop(self):

        self.camera.stop()

    def get_frame(self):

        image = self.camera.get_latest_frame()

        if image is None:
            return None

        self.frame_id += 1

        return Frame(
            image=image,
            timestamp=time.perf_counter(),
            frame_id=self.frame_id,
        )