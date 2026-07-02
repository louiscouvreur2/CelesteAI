from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(slots=True)
class Frame:
    """Image capturée avec son horodatage."""

    image: np.ndarray
    timestamp: float
    frame_id: int