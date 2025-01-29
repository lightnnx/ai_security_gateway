class Config:
    INTERFACE = "eth0"  # Интерфейс для мониторинга
    PACKET_COUNT = 100   # Количество пакетов для анализа
    BLOCKLIST_FILE = "/etc/iptables_blocklist.txt"
    WEB_PORT = 8000      # Порт веб-интерфейса
