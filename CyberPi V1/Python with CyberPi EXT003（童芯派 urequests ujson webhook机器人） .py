""""
名称：EXT 003 童芯派 urequests ujson webhook机器人
硬件： 童芯派 
功能介绍：
在钉钉或飞书等办公IM软件当中，可以添加一些自动发消息的机器人。
通过在软件平台上创建webhook机器人获得webhook机器人链接。
使用micropython的urequests和ujson库（对应python中requests和json库）实现对webhook机器人的信息推送。
结合温湿度传感器获得温湿度的值并推送至机器人上。
注意：不支持中文信息的推送，使用中文信息推送会报错。


难度：⭐⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import urequests
import ujson
import cyberpi
import time


cyberpi.wifi.connect("输入WIFI密码", "输入WIFI密码")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.console.println("已连接至网络")

post_url = "填入webhook机器人的地址"
headers = {'Content-Type': 'application/json'}

while True:
    hum = cyberpi.humiture.get_humidity()
    temp = cyberpi.humiture.get_temp()
    mes = "hum:"+str(hum)+" temp:" + str(temp)
    payload_message = {"msg_type": "text","content": {"text": mes}}
    post_data = ujson.dumps(payload_message)
    payload_message_second = {"msg_type": "text","content": {"text": "temp："+str(temp)}}
    response = urequests.request("POST", url=post_url, data=post_data, headers=headers)
    print(response.text)
    time.sleep(5)
    cyberpi.console.println(response.text)