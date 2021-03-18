# publisher
import paho.mqtt.client as mqtt
import json
import time
import random

client = mqtt.Client()
client.connect('192.168.42.105', 1883)

while True:
    temp = random.randint(0, 40)
    ldr = random.randint(100, 500)
    data = {'temp': temp, 'ldr': ldr}
    data1 = json.dumps(data)

    if temp>25:
        client.publish("topic/fanON", data1)
    else:
        client.publish("topic/fanOFF", data1)

    time.sleep(5)
