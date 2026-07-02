from __future__ import annotations

import time


class FPSCounter:
    """Simple FPS counter."""

    def __init__(self) -> None:
        self.last_time = time.perf_counter()
        self.frames = 0
        self.fps = 0.0

    def update(self) -> float:
        self.frames += 1

        now = time.perf_counter()

        if now - self.last_time >= 1.0:
            self.fps = self.frames / (now - self.last_time)
            self.frames = 0
            self.last_time = now

        return self.fps