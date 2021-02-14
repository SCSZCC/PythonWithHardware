""""
名称：051  MQTT联网警报器 推送端
硬件： 无
功能介绍：
基于在线模式下，获取童芯派灯光传感器的读值，并进行判定,如果光线强度大于一定的数值，
那么给服务器推送警告信息。

难度：⭐⭐⭐⭐

支持的模式：仅支持在线模式

使用到的API及功能解读：
1.paho-mqtt是python中的第三方库，它可以实现与MQTT服务器建立连接，实现通信。
2.paho-mqtt中的使用离不开回调函数的应用。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import paho.mqtt.client as mqtt
import time

client = mqtt.Client()

MQHOST = "请输入服务器地址"
MQPORT = 1883

dict = {}
def mq_connect():
    client.connect(MQHOST, MQPORT, 60)
    client.loop_start()

def on_message_come(client, userdata, msg):
    # print(msg.payload)
    value = msg.payload
    topic = msg.topic
    dict[topic](topic,value)



def on_publish(topic, payload):
    client.publish(topic, payload, 1)


def on_subscribe(topic, callback):
    client.subscribe(topic, 1)
    dict[topic] = callback
    client.on_message = on_message_come



def data(topic,value):
    if value == "emergency":
        while True:
            print("emergency")



mq_connect()
a = 0
on_subscribe("test/123/abc", data)
while True:
    pass






