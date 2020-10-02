""""
名称：045 体感灯光
硬件： 童芯派
功能介绍：实现led灯跟随童芯派姿态的变化而改变位置。

难度：⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
a = 0

cyberpi.led.on('k k b k k')

while True:
    a = cyberpi.get_roll()
    time.sleep(0.2)
    if cyberpi.get_roll() - a > 36:
        cyberpi.led.move(step=1)
    if cyberpi.get_roll() - a < -36:
        cyberpi.led.move(step=-1)


