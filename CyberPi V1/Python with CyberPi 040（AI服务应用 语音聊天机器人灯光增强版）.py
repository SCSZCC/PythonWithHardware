""""
名称：040 语音聊天机器人灯光增强版
硬件： 童芯派
功能介绍：语音聊天机器人加入对童芯派灯光控制的功能。

难度：⭐⭐⭐⭐

支持的模式：仅支持在线模式

使用到的API及功能解读：
1.无新增API



"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
import mkcloud

cyberpi.cloud.setkey("请输入云服务授权码")
cyberpi.console.clear()
cyberpi.console.println("童芯派启动成功！")
cyberpi.wifi.connect("Maker-guest", "makeblock")
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
        if "开灯" in result:
            cyberpi.led.on(255, 255, 255,)
        elif "关灯" in result:
            cyberpi.led.off()
        else:
            response = mkcloud.robot.chat(result)
            cyberpi.led.off()
            cyberpi.console.println(response)
            cyberpi.cloud.tts("chinese", response)


