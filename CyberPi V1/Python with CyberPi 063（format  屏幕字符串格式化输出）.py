""""
名称：063 童芯派 基于format函数的字符串格式化输出
硬件： 童芯派
功能介绍：
基于format函数的字符串格式化输出功能

难度：⭐⭐⭐
支持的模式：在线模式、上传模式
使用到的API及功能解读：
format函数最早出现于Python2.6的版本，相比%占位符的方式，功能更加强大。
format函数中使用{}作为占位符。
在使用中即可以使用默认顺序，也可以依据定义好的顺序对指定的数据进行格式化输出。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi


while True:
    bri = cyberpi.get_bri()
    loud = cyberpi.get_loudness()
    cyberpi.console.println("光线强度为{},声音大小为{}".format(bri, loud))
    cyberpi.console.println("光线强度为{1},声音大小为{0}".format(loud, bri))