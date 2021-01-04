""""
名称：065 童芯派 与一个有趣的网页进行互动
硬件： 童芯派
功能介绍：
配合  https://aidn.jp/mikutap/ 使用。网页是通过键盘按键触发音效。
利用pynput模块给电脑发出键盘指令，进而实现与网页的交互。

难度：⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
from pynput.keyboard import Key, Controller
import time
import random
keyboard = Controller()

charstring = 'abcdefghijklmnopqrstuvwxyz1234567890'
while True:
    if cyberpi.is_shake():
        cyberpi.led.on(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        keychoice = random.choice(charstring)
        keyboard.press(keychoice)
        print(keychoice)
        time.sleep(0.1)