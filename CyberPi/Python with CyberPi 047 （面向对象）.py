""""
名称：047 面向对象(1)
硬件： 童芯派
功能介绍：用屏幕文字来感知面向对象程序的运行。

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


class Screen:
    def __init__(self, name):
        self.name = name
        cyberpi.console.clear()
        time.sleep(1)
        cyberpi.console.println("你创建了" + self.name + "对象并进行了初始化操作")

    def show(self):
        cyberpi.console.println("你好")
        time.sleep(2)
        cyberpi.console.println(self.name + "对象调用了方法show里面的功能")

    def clean(self):
        cyberpi.console.println(self.name + "对象调用了clean方法，即将清空屏幕上的文字")
        cyberpi.console.clear()


hi = Screen("hi")
time.sleep(2)
hi.show()
time.sleep(2)
hi.clean()
