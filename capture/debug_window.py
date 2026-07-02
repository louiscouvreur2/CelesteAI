from __future__ import annotations

import cv2
import numpy as np


class DebugWindow:
    """
    Fenêtre de debug utilisée pendant le développement.
    """

    WINDOW_NAME = "CelesteAI Debug"

    def show(self, image: np.ndarray) -> bool:
        display = (image * 255).astype("uint8")

        cv2.imshow(self.WINDOW_NAME, display)

        key = cv2.waitKey(1)

        return key != 27

    def close(self) -> None:
        cv2.destroyAllWindows()