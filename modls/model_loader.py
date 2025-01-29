import torch
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "anomaly_detector.pth")

def load_model():
    from core.anomaly_detection import AnomalyDetector
    model = AnomalyDetector(input_size=78)  # Замените 78 на фактическое количество признаков
    model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device("cpu")))
    model.eval()
    return model
