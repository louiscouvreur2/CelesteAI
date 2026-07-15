import torch
import torch.nn as nn


class PolicyNetwork(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(15, 64, kernel_size=7, stride=2, padding=3),
            nn.ReLU(),

            nn.Conv2d(64, 128, kernel_size=5, stride=2, padding=2),
            nn.ReLU(),

            nn.Conv2d(128, 128, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),

            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),

            nn.Flatten(),
        )

        with torch.no_grad():

            dummy = torch.zeros(1, 15, 180, 320)

            n = self.features(dummy).shape[1]

        self.classifier = nn.Sequential(

            nn.Linear(n, 1024),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(1024, 512),
            nn.ReLU(),

            nn.Linear(512, 7),

        )

    def forward(self, x):

        x = x.permute(0, 1, 4, 2, 3)

        b, f, c, h, w = x.shape

        x = x.reshape(b, f * c, h, w)

        x = self.features(x)

        x = self.classifier(x)

        return x