from fastapi import FastAPI
from core.packet_sniffer import capture_traffic
from core.preprocess import preprocess_data
from core.anomaly_detection import detect_anomalies
from core.mitigation import mitigate_anomalies

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Network Security Gateway Running"}

@app.get("/monitor")
def monitor_network():
    df = capture_traffic()
    data = preprocess_data(df)
    anomalies = detect_anomalies(data)
    mitigate_anomalies(df, anomalies)

    return {"detected_anomalies": int(sum(anomalies))}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
