from __future__ import annotations

import cv2
import numpy as np


class Resize:

    WIDTH = 320
    HEIGHT = 180

    @classmethod
    def apply(cls, image: np.ndarray) -> np.ndarray:
        return cv2.resize(
            image,
            (cls.WIDTH, cls.HEIGHT),
            interpolation=cv2.INTER_AREA,
        )