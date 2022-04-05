""""
名称：044 灯光排序
硬件： 童芯派
功能介绍：利用sort函数，对灯光点亮的顺序进行排序

难度：⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：

1.sort()函数
python的内建函数，可以对数据进行排序,默认正序排序
sort(reverse = True)   表示倒序排序。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.console.clear()
cyberpi.led.off()
led_id = [1, 3, 2, 5, 4]                  # 定义一个乱序的数列列表
for i in led_id:                          # 根据列表顺序点亮LED灯
    cyberpi.console.print(i)
    cyberpi.led.on('b', id=i)             # id参数，用于填入led顺序的数值
    time.sleep(0.3)
led_id.sort()                             # 对列表led_id进行排序(sort)，默认正序排序
cyberpi.led.off()
cyberpi.console.clear()
for i in led_id:                          # 根据排序后的列表顺序点亮灯光
    cyberpi.console.print(i)
    cyberpi.led.on('b', id=i)
    time.sleep(0.3)
led_id.sort(reverse=True)                 # 对列表led_id进行倒序排序(sort),reverse = True，表示倒序
cyberpi.led.off()
cyberpi.console.clear()
for i in led_id:                          # 根据倒序顺序点亮灯光
    cyberpi.console.print(i)
    cyberpi.led.on('b', id=i)
    time.sleep(0.3)
