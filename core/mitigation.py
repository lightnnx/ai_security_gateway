import os
import subprocess

def block_ip(ip):
    """Блокировка IP через iptables."""
    cmd = f"sudo iptables -A INPUT -s {ip} -j DROP"
    os.system(cmd)

def mitigate_anomalies(df, anomalies):
    """Блокировка атакующих IP-адресов."""
    for i, is_anomalous in enumerate(anomalies):
        if is_anomalous:
            ip = df.iloc[i]["src_ip"]
            print(f"Блокировка подозрительного IP: {ip}")
            block_ip(ip)
