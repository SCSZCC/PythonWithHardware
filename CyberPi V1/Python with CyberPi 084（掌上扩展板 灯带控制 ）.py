""""
名称：084 童芯派 掌上扩展板 灯带流水灯
硬件： 童芯派 灯带 掌上扩展板
功能介绍：
通过童芯派的掌上扩展板驱动灯带，对灯带进行控制，每颗灯珠的颜色随机并实现流水灯的作用。
程序中使用了15颗灯珠的RGB灯带。
程序支持上传模式和在线模式，上传模式效果更好。

使用到的API及功能解读：
1.cyberpi.pocket.led_off(id = "all", port='s1')
熄灭接在扩展板上的灯带的灯珠，id参数填入要熄灭的灯珠位置，port填入灯带接入的接口名称。

2.cyberpi.pocket.led_on(r, g, b, id=i, port='s1')
点亮接在扩展板上的灯带的灯珠，r、g、b参数填入RGB值，数值范围为0-255。
id参数填入要点亮的灯珠位置，port填入灯带接入的接口名称。

3.cyberpi.pocket.led_move(step, cycle, port='s1')
将当前灯光的颜色顺序进行滚动，step表示每次滚动的步长，cycle表示循环的周期，
如灯带的灯珠数为15个，则可以填入15个。如果填入16个，就会发现滚动过程中有颗灯光没点亮，
如果17，则会有两颗，以此类推。
port填入灯带接入的接口名称。


难度：⭐⭐⭐
支持的模式：上传模式、在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time
import random


while True:
    if cyberpi.controller.is_press('a'):
        cyberpi.pocket.led_off(id = "all", port='s1')
        for i in range(1, 16):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            cyberpi.pocket.led_on(r, g, b, id=i, port='s1')
    if cyberpi.controller.is_press('b'):
        cyberpi.pocket.led_off(id = "all", port='s1')
    cyberpi.pocket.led_move(1, 15, port='s1')
    time.sleep(0.2)
        





