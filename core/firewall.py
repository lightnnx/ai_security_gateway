import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

def block_ip(ip_address):
    """Блокирует IP-адрес с помощью iptables."""
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

@app.route("/block_ip", methods=["POST"])
def api_block_ip():
    data = request.get_json()
    ip = data.get("ip")
    if ip and block_ip(ip):
        return jsonify({"status": "success", "message": f"IP {ip} заблокирован"})
    return jsonify({"status": "error", "message": "Не удалось заблокировать IP"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
