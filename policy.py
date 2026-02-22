import torch
import torch.nn as nn

class PolicyNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(4, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )

    def forward(self, state):
        state = torch.tensor(state, dtype=torch.float32)
        prob = self.net(state)
        return prob
