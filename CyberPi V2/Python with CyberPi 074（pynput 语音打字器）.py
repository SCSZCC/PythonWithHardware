""""
名称：074 童芯派 语音打字器
硬件： 童芯派
功能介绍：
利用童芯派的语音识别功能结合pynput模块的键盘控制功能。
将语音识别的结果通过pynput在文档中打出来。
该程序目前只能支持英文。

难度：⭐⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
cyberpi.console.clear()
cyberpi.led.on(0, 0, 0)
cyberpi.set_recognition_url()
cyberpi.cloud.setkey("请输入云服务授权码")    # 通过慧编程账号可以获得
cyberpi.wifi.connect("WIFI名称", "WIFI密码")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.led.on(0,0,255)
cyberpi.console.println("WIFI已连接")
cyberpi.console.println("--------------")
cyberpi.console.println("按下A键开始语音识别")
while True:
    if cyberpi.controller.is_press('a'):
        keyboard.press(Key.space)
        cyberpi.console.clear()
        cyberpi.led.on(100, 0, 0)
        cyberpi.console.println("开始语音识别")
        cyberpi.audio.play("switch")
        cyberpi.console.println("--------------")
        cyberpi.cloud.listen("english", 2)
        cyberpi.led.on(0, 0, 0)
        say = cyberpi.cloud.listen_result()
        cyberpi.console.println(say)
        cyberpi.console.println("--------------")
        for i in say:
            if i == '':
                 keyboard.press(' ')
            else:
                keyboard.press(str(i))
                time.sleep(0.03)
