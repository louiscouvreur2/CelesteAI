import torch

from torch.utils.data import DataLoader, random_split

from learning.dataset import CelesteDataset
from learning.policy_network import PolicyNetwork
from learning.model_manager import ModelManager

from learning.validator import Validator
from learning.scheduler import Scheduler
from learning.checkpoint import Checkpoint
from learning.metrics import Metrics

from learning.evaluator import Evaluator

from learning.history import History

class Trainer:

    def __init__(self):

        self.history = History()

        self.models = ModelManager()

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        dataset = CelesteDataset()

        train_size = int(len(dataset) * 0.8)
        val_size = len(dataset) - train_size

        train_dataset, val_dataset = random_split(
            dataset,
            [train_size, val_size],
        )

        self.loader = DataLoader(
            train_dataset,
            batch_size=8,
            shuffle=True,
        )

        self.validation_loader = DataLoader(
            val_dataset,
            batch_size=8,
            shuffle=False,
        )

        self.model = PolicyNetwork().to(self.device)

        self.optimizer = torch.optim.Adam(
            self.model.parameters(),
            lr=1e-4,
        )

        self.loss_fn = torch.nn.BCEWithLogitsLoss()

        self.scaler = torch.amp.GradScaler(
            "cuda",
            enabled=torch.cuda.is_available(),
        )

        self.validator = Validator(
            self.model,
            self.validation_loader,
            self.loss_fn,
            self.device,
        )

        self.scheduler = Scheduler(
            self.optimizer,
        )

        self.checkpoint = Checkpoint()

        self.evaluator = Evaluator(

            self.model,

            self.validation_loader,

            self.device,

        )


    def train(self, epochs=10):

        self.model.train()

        for epoch in range(epochs):

            total_loss = 0
            total_acc = 0

            for frames, actions in self.loader:

                frames = frames.to(self.device)
                actions = actions.to(self.device)

                self.optimizer.zero_grad()

                logits = self.model(frames)

                loss = self.loss_fn(
                    logits,
                    actions,
                )

                loss.backward()

                self.optimizer.step()

                total_loss += loss.item()

                total_acc += Metrics.binary_accuracy(
                    logits,
                    actions,
                )

            train_loss = total_loss / len(self.loader)
            train_acc = total_acc / len(self.loader)

            val_loss, val_acc = self.validator.validate()

            self.scheduler.step(val_loss)

            print()
            print(f"Epoch {epoch+1}/{epochs}")
            print(f"Train Loss : {train_loss:.4f}")
            print(f"Train Acc  : {train_acc:.4f}")
            print(f"Val Loss   : {val_loss:.4f}")
            print(f"Val Acc    : {val_acc:.4f}")

            self.history.append(

                epoch + 1,

                train_loss,

                train_acc,

                val_loss,

                val_acc,

            )

            if self.checkpoint.is_best(val_loss):

                self.models.save(
                    self.model,
                    "policy_best",
                )

                print("✅ Nouveau meilleur modèle")

        print()

        print("Evaluation finale")

        self.evaluator.evaluate()
