""""
名称：049 MQTT自发自收
硬件： 无
功能介绍：物联网中用到的MQTT通信协议，基于MQTT自发自收

难度：⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.paho-mqtt是python中的第三方库，它可以实现与MQTT服务器建立连接，实现通信。
2.paho-mqtt中的使用离不开回调函数的应用。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import paho.mqtt.client as mqtt
import time

client = mqtt.Client()

MQHOST = "填入服务器地址"
MQPORT = 1883

def mq_connect():
    client.connect(MQHOST, MQPORT, 60)
    client.loop_start()

def on_message_come(client, userdata, msg):
    print(msg.payload)

def on_publish(topic, payload):
    client.publish(topic, payload, 1)

def on_subscribe(topic):
    client.subscribe(topic, 1)
    client.on_message = on_message_come

mq_connect()
a = 0
on_subscribe("test/123/abc")
while True:
    on_publish("test/123/abc", a)
    a += 1
    time.sleep(0.8)




