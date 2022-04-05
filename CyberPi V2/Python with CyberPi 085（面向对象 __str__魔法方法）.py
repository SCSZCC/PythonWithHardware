""""
名称：085 面向对象__str__魔法方法
硬件： 童芯派 
功能介绍：
通过一个简单的程序介绍面向对象当中__str__魔法方法，通过该魔法方法来返回
童芯派光线传感器的读值。

使用到的API及功能解读：
1.self._bri
self._bri指的类定义中定义的bri属性，需要注意的是在bri前面的_,这个并不是属性名称的一部分，
而是指这个属性是一个隐藏属性。即外部无法直接访问对象中的这个属性值。

2.def __str__(self):
这是一个Python面向对象当中常用的魔法方法之一。可以返回类当中的数据，
比如1当中的self._bri的数据就可以通过这个魔法方法返回。但是需要转换成字符型才能返回。
__str__魔法方法通常与print语句一同使用。即通过打印对象名称的方式可以
将数据打印在控制台上。


难度：⭐⭐⭐⭐
支持的模式：上传模式、在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi


class Info:
    def __init__(self):
        cyberpi.display.show_label('对象已被创建', 24, 'center', index=0)

    def get_info(self):
        self._bri = cyberpi.get_bri()

    def __str__(self):
        return str(self._bri)


cy = Info()
cy.get_info()
print(cy)

    