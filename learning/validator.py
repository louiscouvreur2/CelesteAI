import torch

from learning.metrics import Metrics


class Validator:

    def __init__(self, model, loader, loss_fn, device):

        self.model = model

        self.loader = loader

        self.loss_fn = loss_fn

        self.device = device

    @torch.no_grad()

    def validate(self):

        self.model.eval()

        total_loss = 0

        total_acc = 0

        for frames, actions in self.loader:

            frames = frames.to(self.device)

            actions = actions.to(self.device)

            logits = self.model(frames)

            loss = self.loss_fn(logits, actions)

            total_loss += loss.item()

            total_acc += Metrics.binary_accuracy(

                logits,

                actions,

            )

        self.model.train()

        return (

            total_loss / len(self.loader),

            total_acc / len(self.loader),

        )