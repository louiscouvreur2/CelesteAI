import torch

from learning.metrics import Metrics


class Evaluator:

    def __init__(self, model, loader, device):

        self.model = model

        self.loader = loader

        self.device = device

    @torch.no_grad()
    def evaluate(self):

        self.model.eval()

        total = 0

        correct = [0] * 7

        count = [0] * 7

        for frames, actions in self.loader:

            frames = frames.to(self.device)
            actions = actions.to(self.device)

            logits = self.model(frames)

            pred = (torch.sigmoid(logits) > 0.5).float()

            total += Metrics.binary_accuracy(
                logits,
                actions,
            )

            for i in range(7):

                correct[i] += (
                    pred[:, i] == actions[:, i]
                ).sum().item()

                count[i] += actions.shape[0]

        print()

        print("========== EVALUATION ==========")

        names = [

            "UP",
            "LEFT",
            "DOWN",
            "RIGHT",
            "JUMP",
            "GRAB",
            "DASH",

        ]

        for name, c, n in zip(
            names,
            correct,
            count,
        ):

            print(
                f"{name:>5} : {100*c/n:.2f}%"
            )

        print()

        print(
            f"Global : {100*total/len(self.loader):.2f}%"
        )