from pathlib import Path

import torch

from learning.policy_network import PolicyNetwork


class ModelManager:

    def __init__(self):

        self.folder = Path("models")

        self.folder.mkdir(exist_ok=True)

    def save(self, model, name):

        path = self.folder / f"{name}.pt"

        torch.save(model.state_dict(), path)

        print(f"[ModelManager] Saved -> {path}")

    def load(self, name):

        path = self.folder / f"{name}.pt"

        model = PolicyNetwork()

        model.load_state_dict(
            torch.load(path, map_location="cpu")
        )

        model.eval()

        print(f"[ModelManager] Loaded -> {path}")

        return model

    def latest(self):

        files = sorted(self.folder.glob("*.pt"))

        if not files:

            return None

        return files[-1]

    def list_models(self):

        return sorted(self.folder.glob("*.pt"))

    def load_latest(self):

        latest = self.latest()

        if latest is None:
            raise RuntimeError("Aucun modèle trouvé.")

        model = PolicyNetwork()

        model.load_state_dict(
            torch.load(latest, map_location="cpu")
        )

        model.eval()

        return model
