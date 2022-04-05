""""
名称：053  童芯派 汽车转向灯灯效（面向对象）
硬件： 童芯派
功能介绍：利用童芯派的LED灯实现汽车来模拟汽车转向灯效果
        上传模式和在线模式效果有所差异。

难度：⭐⭐⭐⭐

支持的模式：上传、在线都支持


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time


class Led:
    def __init__(self):
        cyberpi.led.off()
        cyberpi.console.clear()

    def direction(self, direct):
        self.direct = direct
        if self.direct == "left":
            self.sequence = 'y y k k k '
        if self.direct == "right":
            self.sequence = 'k k k y y '
        if self.direct == "straight":
            self.sequence = 'k k k k k '
        if self.direct == "emergency":
            self.sequence = 'y y k y y '

    def blink(self):
        cyberpi.led.show(self.sequence)
        time.sleep(0.1)
        cyberpi.led.off()
        time.sleep(0.1)




car = Led()
status = 0
while True:
    if cyberpi.controller.is_press("up"):
       status += 1
    if cyberpi.controller.is_press("down"):
       status -= 1
    if status == 1:
        car.direction("left")
    elif status == 2:
        status = 1
    elif status == 0:
        car.direction("straight")
    elif status == -1:
        car.direction("right")
    elif status == -2:
        status = -1
    car.blink()
