import cv2

from PySide6.QtGui import QImage


class FrameConverter:

    @staticmethod
    def to_qimage(frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, c = rgb.shape

        bytes_per_line = c * w

        return QImage(
            rgb.data,
            w,
            h,
            bytes_per_line,
            QImage.Format_RGB888,
        ).copy()