from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class GameState:
    """
    Ce que voit l'IA.
    """

    frame: np.ndarray

    frame_id: int

    timestamp: float