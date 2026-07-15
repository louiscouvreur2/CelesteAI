class Checkpoint:

    def __init__(self):

        self.best_loss = float("inf")

    def is_best(self, loss):

        if loss < self.best_loss:

            self.best_loss = loss

            return True

        return False