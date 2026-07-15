import torch


class TensorConverter:

    @staticmethod
    def to_tensor(array):

        tensor = torch.from_numpy(array)

        return tensor.float()