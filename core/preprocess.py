from sklearn.preprocessing import StandardScaler
import numpy as np

scaler = StandardScaler()

def preprocess_data(df):
    """Преобразование захваченных данных в формат, подходящий для модели."""
    if df.empty:
        return None
    
    numeric_features = ["length", "protocol", "flags"]
    df[numeric_features] = scaler.fit_transform(df[numeric_features])

    return np.array(df[numeric_features], dtype=np.float32)
