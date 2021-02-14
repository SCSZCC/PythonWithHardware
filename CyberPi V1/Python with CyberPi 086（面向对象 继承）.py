""""
名称：086 面向对象继承
硬件： 童芯派
功能介绍：
通过一个简单的程序来了解面向对象继承。
童芯派光线传感器的读值。

使用到的API及功能解读：
1.class Child(Father):
Child类后面的括号中填写的Father表示继承Child类继承了Father类，
也就是说Child类具备了Father类相同的方法、功能。通过继承的方式可以提高代码的复用性。



难度：⭐⭐⭐⭐⭐
支持的模式：上传模式、在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time


class Father:
    def show(self):
        for i in range(1,6):
            cyberpi.led.on('b', id=i)
            time.sleep(0.2)
        cyberpi.led.off()


class Child(Father):
    pass


first = Father()
cyberpi.console.println('这是根据Father类创建出的对象')
cyberpi.console.println('调用show方法')
first.show()
time.sleep(3)
second = Child()
cyberpi.console.clear()
cyberpi.console.println('这是根据Child类创建出的对象')
cyberpi.console.println('调用show方法')
second.show()

    