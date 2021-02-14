""""
名称：036 童芯派的TTS功能
硬件： 童芯派
功能介绍：结合语音识别与文字转语音功能（TTS）,将识别的结果说出来。

难度：⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1. cyberpi.cloud.tts(language, message)
  朗读对应文本。参数：
• language str，有效值为："chinese"：汉语；"english"：英语；表示需要朗读的语种。
• message str，表示朗读的文本内容。

2.cyberpi.cloud.translate(language, message)
  翻译对应语种的文本。参数：
• language str，有效值为："chinese"：中文；"english"：英文；表示需要翻译为的语种。
• message str，表示需要翻译的文本内容。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.cloud.setkey("请输入自己的云服务授权码")
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
        cyberpi.cloud.tts("chinese", result)
        translate = cyberpi.cloud.translate("english", result)
        cyberpi.console.println(translate)
