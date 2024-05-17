# pip install "paho-mqtt<2.0.0"
# 1.6 is a lot better ducment than the newly release 2.0.0 that breaks backwards compatibilty
# This code is written with 1.6 in mind and will not work for paho 2.0
import paho.mqtt.client as mqtt
import time
import sys

import tkinter as tk
import random

msg = []
# Replace the 4 x with the info on your paper sheet
broker_address = "mqtt.ics.ele.tue.nl"
topic_publish = "/pynqbridge/23/send"
topic_subscribe = "/pynqbridge/23/recv"
username = "Student45"  # Replace with your MQTT username
password = "di1BuX2i"  # Replace with your MQTT password

if sys.argv[1] == "1":
    # if you pass the argument 1 in while running the code
    # it will swap the topic and publich for easer testing of the message on it
    topic_publish, topic_subscribe = topic_subscribe, topic_publish

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
    print("Received message: " + msg + " on topic " + message.topic)


# Setup MQTT client and callbacks
client = mqtt.Client("MQTT_Example", clean_session=True)
client.on_connect = on_connect
client.on_message = on_message

# Set the username and password
client.username_pw_set(username, password)

# Connect to MQTT broker
try:
    client.connect(broker_address, port=1883)
except Exception as e:
    print(f"Failed to connect to MQTT broker at {broker_address}: {e}")
    exit(1)

client.disconnect()
