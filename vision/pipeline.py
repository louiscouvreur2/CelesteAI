from __future__ import annotations

import numpy as np

from vision.resize import Resize
from vision.normalize import Normalize


class VisionPipeline:
    """
    Pipeline de prétraitement des images.
    """

    def process(self, image: np.ndarray) -> np.ndarray:
        image = Resize.apply(image)
        image = Normalize.apply(image)
        return image