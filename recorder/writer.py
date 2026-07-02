from pathlib import Path

import cv2

from capture.frame import Frame


class FrameWriter:

    def __init__(self, folder: Path):

        self.folder = folder

    def write(self, frame: Frame):

        filename = self.folder / f"{frame.frame_id:08}.jpg"

        cv2.imwrite(str(filename), frame.image)