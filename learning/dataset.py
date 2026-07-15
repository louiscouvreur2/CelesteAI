from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset


class CelesteDataset(Dataset):

    def __init__(self, folder="recordings"):

        self.folder = Path(folder)

        self.index = []

        self.cache = {}

        for file in sorted(self.folder.glob("*.npz")):

            print(f"Indexation : {file.name}")

            data = np.load(file, mmap_mode="r")

            n = len(data["frames"])

            for i in range(n):

                self.index.append(
                    (
                        file,
                        i,
                    )
                )

        print()
        print(f"{len(self.index)} échantillons indexés.")

    def __len__(self):

        return len(self.index)

    def _load(self, file):

        key = str(file)

        if key not in self.cache:

            self.cache[key] = np.load(
                file,
                mmap_mode="r",
            )

        return self.cache[key]

    def __getitem__(self, idx):

        file, sample = self.index[idx]

        data = self._load(file)

        frame = data["frames"][sample]

        action = data["actions"][sample]

        frame = (
            torch.from_numpy(frame)
            .float()
            .div(255.0)
        )

        action = torch.from_numpy(action).float()

        return frame, action