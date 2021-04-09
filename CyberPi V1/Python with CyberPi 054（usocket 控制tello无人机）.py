""""
名称：054  童芯派控制Tello无人机（MicroPython usocket标准库）
硬件： 童芯派
功能介绍：简单的利用童芯派实现对Tello无人机的起飞降落控制。

难度：⭐⭐⭐⭐⭐⭐

支持的模式：上传

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------


import usocket
import cyberpi
import time
import sys


cyberpi.wifi.connect("TELLO-5A186C", "")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.console.println("已连接至网络")



host = ''
port = 9000
locaddr = usocket.getaddrinfo(host, port)[0][-1]
print(locaddr)
sock = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)
msg = None


while True:
    if cyberpi.controller.is_press("up"):
        cyberpi.console.println("command")
        msg = b"command"
        # msg = msg.encode()
        sock.sendto(msg, tello_address)
        time.sleep(0.5)
    if cyberpi.controller.is_press("a"):
        cyberpi.console.println("off")
        msg = "takeoff"
        msg = msg.encode()
        sent = sock.sendto(msg, tello_address)
        time.sleep(0.5)
    if cyberpi.controller.is_press("b"):
        cyberpi.console.println("off")
        msg = "land"
        msg = msg.encode()
        sock.sendto(msg, tello_address)
        time.sleep(0.5)