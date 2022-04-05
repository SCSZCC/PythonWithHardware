""""
名称：014 今天开什么颜色的灯(2)
硬件：童芯派
功能介绍：通过输入信息，控制童芯派灯光的颜色

难度：⭐⭐

支持的模式：在线

使用功能解读：
1. 双分支结构
if-条件成立 :
----条件成立执行的代码
else:
----条件不成立时执行的代码

if-else共同构成一个双分支结构。

- 表示空格
条件成立，返回值则为True，条件不成立则返回值False


"""
#---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import random

cyberpi.led.off()                                                # 熄灭所有LED灯，进行灯光初始化
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
light_color = input("今天要开随机灯光还是白灯？（请输入白灯或者其它） ")  # 用input提示可以输入的灯光颜色并存放在变量light_color当中
if light_color == "白灯":                                         # 用if判断light_color中的数据是否为“白灯”
    cyberpi.led.on(255, 255, 255)                                    # 条件成立则打开白色的灯光
else:                                                             # 否则:
    cyberpi.led.on(r, g, b)                                          # 打开随机灯光