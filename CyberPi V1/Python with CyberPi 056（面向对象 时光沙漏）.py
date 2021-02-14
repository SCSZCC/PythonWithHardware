""""
名称：056 灯光沙漏
硬件： 童芯派 + 掌上扩展板
功能介绍：
利用童芯派的加速度传感器自作一个根据姿态调整的时光沙漏。
当然是没有计时效果的。

难度：⭐⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
面向对象，类的方法调用自己的方法使用 self.方法名 方式进行调用。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
import random

class SandyClock():
    def __init__(self):
        cyberpi.led.off()
        self.id = 1
        self.led_color()

    def get_status(self, status):
        self.status = status

    def led_color(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def clock_direction(self):
        if self.status == 'clockwise':
            self.id += 1
            if self.id > 5:
                self.id = 1
                self.led_color()
        if self.status == 'counterclockwise':
            self.id -= 1
            if self.id <= 0:
                self.id = 5
                self.led_color()

    def led_move(self):
        cyberpi.led.on(self.r, self.g, self.b, id=self.id)
        time.sleep(0.2)
        cyberpi.led.off()


clock = SandyClock()
while True:
    if cyberpi.get_acc('x') > 9:
        clock.get_status('clockwise')
    if cyberpi.get_acc('x') < -9:
        clock.get_status('counterclockwise')
    clock.clock_direction()
    clock.led_move()






