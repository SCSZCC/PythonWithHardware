""""
名称：087 面向对象 多态
硬件： 童芯派
功能介绍：
通过一个简单的程序来了解面向对象多态。
通过童芯派的灯光控制进行呈现。

使用到的API及功能解读：
1.关于多态
多态的指不同的类创建出的对象执行相同名称的方法，得到的是不同的结果。
子类重写父类是多态的一种表现。示例程序当中子类继承了父类的show方法，
但是子类觉得父类的方法不满足自己的需求，于是它可以重写show方法，实现
了不同的功能。



难度：⭐⭐⭐⭐⭐
支持的模式：上传模式、在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time


class First:
    def show(self):
        for i in range(1,6):
            cyberpi.led.on('b', id=i)
            time.sleep(0.2)
        cyberpi.led.off()


class Second(First):
    def show(self):
        for i in range(5, 0, -1):
            cyberpi.led.on('r', id=i)
            time.sleep(0.2)
        cyberpi.led.off()


a = First()
cyberpi.console.println('这是根据First类创建出的对象')
cyberpi.console.println('调用show方法')
a.show()
time.sleep(3)
b = Second()
cyberpi.console.clear()
cyberpi.console.println('这是根据Child类创建出的对象')
cyberpi.console.println('调用show方法')
b.show()
