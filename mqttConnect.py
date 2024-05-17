import paho.mqtt.client as mqtt
import sys

# MQTT configuration
broker_address = "mqtt.ics.ele.tue.nl"
topic_publish = "/pynqbridge/23/send"
topic_subscribe = "/pynqbridge/23/recv"
username = "Student45"
password = "di1BuX2i"

# Callback when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic_subscribe, qos=1)
    else:
        print(f"Failed to connect, return code {rc}\n")

# Callback when receiving a message from the MQTT broker
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("Received message:", msg, "on topic", message.topic)
    # Process the received message here...

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client("MQTT_Example", clean_session=True)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(username, password)

    def connect(self):
        try:
            self.client.connect(broker_address, port=1883)
        except Exception as e:
            print(f"Failed to connect to MQTT broker at {broker_address}: {e}")
            sys.exit(1)

    def disconnect(self):
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        on_connect(client, userdata, flags, rc)

    def on_message(self, client, userdata, message):
        on_message(client, userdata, message)

if __name__ == "__main__":
    client = MQTTClient()
    client.connect()

    # Continue with your main program logic...

    # Don't forget to disconnect when done
    client.disconnect()
predefined_points = [
    (5, 5, "blue", "oval", 5),
    (-5, 5, "green", "rectangle", 3),
    (20, -15, "red", "oval", 4),
    (-15, -5, "purple", "rectangle", 6)
]
