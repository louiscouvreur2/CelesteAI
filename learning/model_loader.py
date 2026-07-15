import torch

from learning.policy_network import PolicyNetwork


class ModelLoader:

    @staticmethod
    def load(path):

        model = PolicyNetwork()

        model.load_state_dict(
            torch.load(
                path,
                map_location="cpu",
            )
        )

        model.eval()

        return model