from fastapi import APIRouter
from core.packet_sniffer import capture_traffic
from core.preprocess import preprocess_data
from core.anomaly_detection import detect_anomalies
from core.mitigation import mitigate_anomalies

router = APIRouter()

@router.get("/monitor")
def monitor_network():
    """Мониторинг сети, обнаружение аномалий и их устранение."""
    df = capture_traffic()
    data = preprocess_data(df)
    anomalies = detect_anomalies(data)
    mitigate_anomalies(df, anomalies)

    return {"detected_anomalies": int(sum(anomalies))}

@router.get("/status")
def get_status():
    """Возвращает статус сервиса."""
    return {"status": "running", "message": "AI Network Security Gateway Active"}

@router.get("/blocklist")
def get_blocked_ips():
    """Возвращает список заблокированных IP-адресов."""
    try:
        with open("/etc/iptables_blocklist.txt", "r") as f:
            blocked_ips = f.readlines()
        return {"blocked_ips": [ip.strip() for ip in blocked_ips]}
    except FileNotFoundError:
        return {"blocked_ips": []}
