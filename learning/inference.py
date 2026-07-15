import torch

from learning.policy_network import PolicyNetwork


class Inference:

    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = PolicyNetwork().to(self.device)

        self.model.eval()

    @torch.no_grad()
    def predict(self, frames):

        tensor = torch.from_numpy(frames)

        tensor = tensor.unsqueeze(0)

        tensor = tensor.float()

        tensor = tensor.to(self.device)

        logits = self.model(tensor)

        return (torch.sigmoid(logits) > 0.5).cpu().numpy()[0]