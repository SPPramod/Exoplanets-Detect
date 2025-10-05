import torch

class Perceptron(torch.nn.Module):
    def __init__(self, sizes = [3197, 1000, 250, 20], output = 2):
        super(Perceptron, self).__init__()
        self.fc1 = torch.nn.Linear(sizes[0], sizes[1])
        self.fc2 = torch.nn.Linear(sizes[1], sizes[2])
        self.fc3 = torch.nn.Linear(sizes[2], sizes[3])
        self.fc4 = torch.nn.Linear(sizes[3], output)
        self.relu = torch.nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x