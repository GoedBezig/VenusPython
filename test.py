import tkinter as tk
import json
import paho.mqtt.client as mqtt

# MQTT Broker details
broker_address = "mqtt.ics.ele.tue.nl"
topic_subscribe = "/pynqbridge/23/send"
username = "Student45"  # Replace with your MQTT username
password = "di1BuX2i"  # Replace with your MQTT password

def create_block(x, y, width, height, color):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    canvas.pack()

    # Draw x-axis
    canvas.create_line(20, 200, 380, 200, arrow=tk.LAST)
    canvas.create_text(380, 210, text='X', font=('Helvetica', 10))

    # Draw y-axis
    canvas.create_line(200, 380, 200, 20, arrow=tk.LAST)
    canvas.create_text(190, 20, text='Y', font=('Helvetica', 10))

    # Draw grid lines
    for i in range(1, 20):
        canvas.create_line(20 * i, 0, 20 * i, 400, dash=(2, 2), fill='gray')
        canvas.create_line(0, 20 * i, 400, 20 * i, dash=(2, 2), fill='gray')

    # Draw the rectangle
    canvas.create_rectangle(x, y, x + width, y + height, fill=color)

    root.mainloop()

# Callback when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # Subscribe to the specified topic
        client.subscribe(topic_subscribe)
    else:
        print(f"Failed to connect, return code {rc}\n")

# Callback when receiving a message from the MQTT broker
def on_message(client, userdata, message):
    # Decode the JSON message and convert it to a Python dictionary
    #print("Received JSON message:", json_data)

    json_data = json.loads(message.payload.decode('utf-8'))
    x = json_data.get('x', 0)  # Default to 0 if 'x' key is not found
    y = json_data.get('y', 0)  # Default to 0 if 'y' key is not found
    width = json_data.get('width', 50)  # Default to 50 if 'width' key is not found
    height = json_data.get('height', 50)  # Default to 50 if 'height' key is not found
    color = json_data.get('color', 'blue')  # Default to 'blue' if 'color' key is not found
    create_block(x, y, width, height, color)

# Create an MQTT client instance
client = mqtt.Client()

# Set the username and password
client.username_pw_set(username, password)

# Set up the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address)

# Start the loop to process network traffic and dispatch callbacks
client.loop_forever()