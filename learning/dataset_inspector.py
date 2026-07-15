from pathlib import Path

import numpy as np


class DatasetInspector:

    def __init__(self, folder="recordings"):

        self.folder = Path(folder)

    def inspect(self):

        files = sorted(self.folder.glob("*.npz"))

        total_frames = 0

        total_seconds = 0

        print()

        print("========== DATASET ==========")

        print()

        print(f"Sessions : {len(files)}")

        print()

        for file in files:

            data = np.load(file)

            frames = data["frames"]

            fps = 60

            seconds = len(frames) / fps

            total_frames += len(frames)

            total_seconds += seconds

            print(

                f"{file.name:<20}"

                f"{len(frames):5d} frames"

                f"   {seconds:6.1f} sec"

            )

        print()

        print("-----------------------------")

        print()

        print(f"Frames total : {total_frames}")

        print(f"Temps total  : {total_seconds:.1f} sec")

        print(f"Heures       : {total_seconds/3600:.3f}")