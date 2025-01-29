import torch
import numpy as np
from models.model_loader import load_model

class AnomalyDetector(torch.nn.Module):
    def __init__(self, input_size):
        super(AnomalyDetector, self).__init__()
        self.network = torch.nn.Sequential(
            torch.nn.Linear(input_size, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, 32),
            torch.nn.ReLU(),
            torch.nn.Linear(32, 1),
            torch.nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)

model = load_model()

def detect_anomalies(data):
    """Анализ данных и определение аномалий."""
    if data is None:
        return []
    
    tensor_data = torch.tensor(data, dtype=torch.float32)
    with torch.no_grad():
        predictions = model(tensor_data).squeeze()
    
    anomalies = (predictions > 0.5).numpy()
    return anomalies
