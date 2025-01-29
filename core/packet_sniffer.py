from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import numpy as np

def packet_callback(packet):
    """Функция обработки захваченного пакета."""
    if packet.haslayer(IP):
        data = {
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "protocol": packet[IP].proto,
            "length": len(packet),
            "flags": packet[TCP].flags if packet.haslayer(TCP) else 0,
        }
        return data
    return None

def capture_traffic(interface="eth0", count=100):
    """Захват сетевого трафика и возврат в формате DataFrame."""
    packets = sniff(iface=interface, count=count, prn=packet_callback, store=False)
    df = pd.DataFrame([pkt for pkt in packets if pkt is not None])
    return df
