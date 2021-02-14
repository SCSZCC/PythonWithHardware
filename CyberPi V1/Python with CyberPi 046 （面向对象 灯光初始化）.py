""""
名称：046 面向对象(1)
硬件： 童芯派
功能介绍：利用面向对象语法对灯光的功能进行初始化。

难度：⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.class 关键字
用于定义类，class后面一般跟着类的名字。类的名字采用大驼峰命名法。

2.__init__  初始化方法
用于类的功能初始化。在创建对象的时候可以进行一些功能上的初始化操作。也可以传递参数。

3.面向对象。
Python是一门面向对象的面向的语言，面向对象是一个抽象的概念。无论是常用的Print函数，还是input函数，本质上都是一个对象。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time


class Basic:
    def __init__(self):
        cyberpi.led.off()
        cyberpi.console.clear()
        cyberpi.console.print("模块初始化了")
        time.sleep(1)

    def blue(self):
        cyberpi.led.on('b')

    def green(self):
        cyberpi.led.on('g')

    def red(self):
        cyberpi.led.on('r')


light = Basic()
while True:
    light.blue()
    time.sleep(1)
    light.green()
    time.sleep(1)
    light.red()
    time.sleep(1)


