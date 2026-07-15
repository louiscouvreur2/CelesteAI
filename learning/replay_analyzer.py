from pathlib import Path

import numpy as np


class ReplayAnalyzer:

    ACTIONS = [
        "UP",
        "LEFT",
        "DOWN",
        "RIGHT",
        "JUMP",
        "GRAB",
        "DASH",
    ]

    def __init__(self, folder="recordings"):

        self.folder = Path(folder)

    def analyze(self):

        counts = np.zeros(7, dtype=np.int64)

        total_frames = 0

        for file in self.folder.glob("*.npz"):

            data = np.load(file)

            actions = data["actions"]

            counts += actions.sum(axis=0).astype(np.int64)

            total_frames += len(actions)

        print()

        print("========== DATASET ==========")

        print(f"Frames : {total_frames}")

        print()

        for name, value in zip(self.ACTIONS, counts):

            percent = value / total_frames * 100

            print(
                f"{name:>6} : "
                f"{value:7d} "
                f"({percent:5.2f}%)"
            )