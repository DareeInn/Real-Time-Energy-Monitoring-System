import paho.mqtt.client as mqtt
import json
from .database import save_reading

MQTT_BROKER = 'localhost'
MQTT_TOPIC = 'home/energy'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        save_reading(payload)
        print("Saved reading:", payload)
    except Exception as e:
        print("Failed to save reading:", e)

def start_monitor():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, 1883, 60)
    client.loop_start()
