""""
名称：061 童芯派 精灵 语音识别转二维码
硬件： 童芯派
功能介绍：
将语音识别的结果通过二维码的方式进行呈现。

难度：⭐⭐⭐⭐⭐
支持的模式：仅支持上传模式，请使用慧编程Python进行程序编写和程序烧录。
使用到的API及功能解读：

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import random
import time


def draw():
    cyberpi.sketch.start()
    cyberpi.sketch.set_size(5)
    cyberpi.sketch.move_to(0, 0)
    cyberpi.sketch.set_speed(16)
    cyberpi.sketch.set_color(255, 255, 255)
    for i in range(1, 5, 1):
        for j in range(0, 8, 1):
            cyberpi.sketch.move(16)
        cyberpi.sketch.cw(90)
    cyberpi.sketch.end()



cyberpi.cloud.setkey("请输入云服务授权码")
cyberpi.console.clear()
cyberpi.console.println("童芯派启动成功！")
cyberpi.wifi.connect("Maker-guest", "makeblock")
cyberpi.console.println("WIFI连接中...")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.led.on(0, 0, 255)
cyberpi.console.clear()
cyberpi.display.show_label("WiFi连接成功", 16, "center", index=0)
time.sleep(1)

draw()
while True:
    if cyberpi.controller.is_press("a"):
        cyberpi.console.clear()
        cyberpi.console.println("开始语音识别")
        cyberpi.led.on(0, 255, 0)
        cyberpi.cloud.listen("chinese", 2)
        result = cyberpi.cloud.listen_result()
        qrcode = cyberpi.sprite()
        qrcode.draw_qrcode(result)
        qrcode.set_size(size=300)
        cyberpi.screen.render()
