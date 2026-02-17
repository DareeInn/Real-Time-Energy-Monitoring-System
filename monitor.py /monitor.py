import time
import json
import requests
import paho.mqtt.client as mqtt

MQTT_BROKER = 'localhost'
MQTT_TOPIC = 'home/energy'
SHELLY_IP = 'http://192.168.50.163'  # Replace with your plug’s IP if needed

def fetch_energy_data():
    try:
        response = requests.get(f"{SHELLY_IP}/rpc/Switch.GetStatus?id=0", timeout=5)
        data = response.json()
        power = data['aenergy']['by_minute'][-1]
        total = data['aenergy']['total']
        return {
            'power': power,
            'total': total,
            'timestamp': time.time()
        }
    except Exception as e:
        print("Error fetching data:", e)
        return None

def publish_loop():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    client.loop_start()

    while True:
        reading = fetch_energy_data()
        if reading:
            payload = json.dumps(reading)
            client.publish(MQTT_TOPIC, payload)
            print("Published:", payload)
        time.sleep(2)

if __name__ == '__main__':
    publish_loop()
