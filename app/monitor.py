from flask import Blueprint, jsonify
import requests

monitor_bp = Blueprint("monitor", __name__)

SHELLY_IP = "192.168.50.163"  # Change this if your plug IP is different

@monitor_bp.route("/api/status")
def get_status():
    try:
        response = requests.get(f"http://{SHELLY_IP}/rpc/Switch.GetStatus?id=0")
        data = response.json()
        power = data['aenergy']['by_minute'][-1]
        total = data['aenergy']['total']
        return jsonify({"power": power, "total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
