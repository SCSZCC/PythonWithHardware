""""
名称：048 回调函数
硬件： 童芯派
功能介绍：用硬件来了解回调函数。

难度：⭐⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.@是python的一个装饰器，针对函数，起调用传参的作用。
2.回调函数可以在不修改函数代码的基础上给代码添加新的功能。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

def Led(func):
    cyberpi.console.clear()
    func()
    time.sleep(2)

@Led
def Hi():
    cyberpi.console.println("Hello")
    cyberpi.led.on(0, 0, 255)

@Led
def Hello():
    cyberpi.console.println("你好")
    cyberpi.led.on(255, 0, 0)


