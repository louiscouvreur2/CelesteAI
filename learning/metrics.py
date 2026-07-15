import torch


class Metrics:

    @staticmethod
    def binary_accuracy(logits, targets):

        prediction = (torch.sigmoid(logits) > 0.5).float()

        correct = (prediction == targets).float()

        return correct.mean().item()