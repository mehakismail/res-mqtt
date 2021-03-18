# subscriber
import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect('192.168.42.105', 1883)


def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    client.subscribe("topic/fanON")
    client.subscribe("topic/fanOFF")


def on_message(client, userdata, message):
    print(message.payload.decode())
    # Receive data and decode it
    print("topic:", message.topic)
    print("Message received: " + message.payload.decode('utf-8'))
    data = json.loads(message.payload.decode('utf-8'))
    print(data)

    if message.topic == "topic/fanON":
        print("Fan is ON")

    if message.topic == "topic/fanOFF":
        print("Fan is OFF")

    print()


while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
