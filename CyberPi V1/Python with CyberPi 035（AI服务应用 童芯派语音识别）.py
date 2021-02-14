""""
名称：035 童芯派的语音识别
硬件： 童芯派
功能介绍：童芯派设置了云服务授权码，并连接WIFI后可以，调用云服务相关的API实现，语音识别功能。
        当按键A按下，开始语音识别，屏幕上识别语音识别后的结果。

难度：⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1. cyberpi.cloud.listen(str, int)
   童芯派语音识别API,str处填入要识别的语言，如“chinese”,int处填入时间
   表示要语音识别的时间。

2.cyberpi.cloud.listen_result()
  语音识别结果的API，返回的结果可以存放在变量当中。



"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.cloud.setkey("填入你的云服务授权码")
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

while True:
    if cyberpi.controller.is_press("a"):
        cyberpi.console.clear()
        cyberpi.console.println("开始语音识别")
        cyberpi.led.on(0, 255, 0)
        cyberpi.cloud.listen("chinese", 2)
        result = cyberpi.cloud.listen_result()
        cyberpi.console.println("识别结果： " + result)
        cyberpi.led.off()

