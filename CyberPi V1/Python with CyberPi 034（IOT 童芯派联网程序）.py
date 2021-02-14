""""
名称：034 童芯派的联网
硬件： 童芯派
功能介绍：实现童芯派的联网功能。

难度：⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.cyberpi.cloud.setkey("输入你的云服务授权码")
  设置云服务的授权码

2.cyberpi.wifi.connect("wifi名称", "密码")
  设置wifi的名称和密码，连接到指定wifi。

3.cyberpi.wifi.is_connect()
  返回童芯派wifi连接状态。



"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.cloud.setkey("输入你的云服务授权码")
cyberpi.console.clear()
cyberpi.console.println("童芯派启动成功！")
cyberpi.wifi.connect("输入WIFI名称", "输入WIFI密码")
cyberpi.console.println("WIFI连接中...")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.led.on(0, 0, 255)
cyberpi.console.clear()
cyberpi.display.label("WiFi连接成功", 16, "center")
time.sleep(1)