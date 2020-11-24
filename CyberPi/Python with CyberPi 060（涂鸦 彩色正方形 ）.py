""""
名称：060 童芯派 涂鸦 彩色方块
硬件： 童芯派
功能介绍：
使用童芯派的屏幕涂鸦功能，在屏幕上绘制彩色方块
难度：⭐⭐⭐⭐⭐
支持的模式：仅支持上传模式，请使用慧编程Python进行程序编写和程序烧录。
使用到的API及功能解读：
1.开始涂鸦  cyberpi.sketch.start()
    相当于落笔
2.定义绘制的像素尺寸。  cyberpi.sketch.set_size(int)
  相当于设置线宽
3.将喷枪移动到指定位置 cyberpi.sketch.move_to(0, 0)
  移动到指定位置
4.设定绘图速度 cyberpi.sketch.set_speed(int)
  绘图速度需要与cyberpi.sketch.move(int)API的参数相匹配。
5.设置每次绘制的长度  cyberpi.sketch.move(int)
  及一次绘制多长的线段
6.顺时针转向 cyberpi.sketch.cw(int)
  调整绘制的的方向，配合cyberpi.sketch.move(int)使用
7.结束涂鸦 cyberpi.sketch.end()
  相当于抬笔
"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import random


def draw():
    cyberpi.sketch.start()
    cyberpi.sketch.set_size(1)
    cyberpi.sketch.move_to(0, 0)
    cyberpi.sketch.set_speed(16)
    x = 0
    y = 0
    for k in range(0, 9, 1):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        cyberpi.led.on(r, g, b)
        cyberpi.sketch.set_color(r, g, b)
        for i in range(1, 5, 1):
            for j in range(0, 8 - k, 1):
                cyberpi.sketch.move(16)
            cyberpi.sketch.cw(90)
        x += 8
        y += 8
        cyberpi.sketch.move_to(x, y)
    cyberpi.sketch.end()
    cyberpi.led.off()


while True:
    if cyberpi.controller.is_press('a'):
        draw()
    if cyberpi.controller.is_press('b'):
        cyberpi.sketch.clear()