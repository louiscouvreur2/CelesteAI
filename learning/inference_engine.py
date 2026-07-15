import numpy as np
import torch

from learning.model_manager import ModelManager


class InferenceEngine:

    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = ModelManager().load("policy_best")

        self.model.to(self.device)

        self.model.eval()

    @torch.no_grad()
    def predict(self, state):

        if not isinstance(state, np.ndarray):
            state = np.asarray(state)

        tensor = (
            torch.from_numpy(state)
            .float()
            .unsqueeze(0)
            .to(self.device)
        )

        logits = self.model(tensor)

        prediction = (
            torch.sigmoid(logits) > 0.5
        )

        return prediction.squeeze(0).cpu().numpy()