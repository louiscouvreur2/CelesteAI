from pathlib import Path
import csv


class History:

    def __init__(self):

        self.file = Path("models/history.csv")

        self.file.parent.mkdir(exist_ok=True)

        if not self.file.exists():

            with open(self.file, "w", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "epoch",
                    "train_loss",
                    "train_acc",
                    "val_loss",
                    "val_acc",
                ])

    def append(
        self,
        epoch,
        train_loss,
        train_acc,
        val_loss,
        val_acc,
    ):

        with open(self.file, "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                epoch,
                train_loss,
                train_acc,
                val_loss,
                val_acc,
            ])