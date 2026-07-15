import torch


class Scheduler:

    def __init__(self, optimizer):

        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(

            optimizer,

            mode="min",

            factor=0.5,

            patience=3,

        )

    def step(self, loss):

        self.scheduler.step(loss)