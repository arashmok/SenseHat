import time
import paho.mqtt.client as mqtt
from sense_hat import SenseHat


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))

    if ((str(msg.payload) == "on") and (msg.topic == "node2/led")):
        SenseHat().show_message("ON", text_colour=[255, 0, 0])
    elif str((msg.payload) == "off") and (msg.topic == "node2/led"):
        SenseHat().show_message("OFF", text_colour=[255, 0, 0])
    elif (str(msg.payload == "true") and (msg.topic == "node2/temp/req")):
        arvanClient.publish("node2/room/temp", int(SenseHat().temp) - 10)


arvanClient = mqtt.Client()
# client.on_connect = on_connect
arvanClient.on_message = on_message

arvanClient.connect("185.97.117.228", 11883, 60)
# arvanClient.publish("node2/room/temp", round(weather.temperature()))
arvanClient.subscribe("node2/temp/req")
arvanClient.subscribe("node2/led")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
arvanClient.loop_forever()
