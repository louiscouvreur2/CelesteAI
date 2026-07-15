from pathlib import Path
import numpy as np


class DatasetWriter:

    def __init__(self):
        self.folder = Path("recordings")
        self.folder.mkdir(parents=True, exist_ok=True)

    def save(self, session):

        files = sorted(self.folder.glob("session_*.npz"))
        index = len(files) + 1

        filename = self.folder / f"session_{index:04d}.npz"

        frames = np.asarray(session.frames, dtype=np.uint8)
        actions = np.asarray(session.actions, dtype=np.uint8)
        timestamps = np.asarray(session.timestamps, dtype=np.float64)

        print("Frames dtype :", frames.dtype)
        print("Frames shape :", frames.shape)

        np.savez_compressed(
            filename,
            frames=frames,
            actions=actions,
            timestamps=timestamps,
        )

        print(f"[Recorder] Sauvegardé : {filename}")
        print(f"[Recorder] Frames : {len(frames)}")