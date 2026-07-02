from __future__ import annotations

import numpy as np


class Normalize:

    @staticmethod
    def apply(image: np.ndarray) -> np.ndarray:
        image = image.astype(np.float32)
        image /= 255.0
        return image