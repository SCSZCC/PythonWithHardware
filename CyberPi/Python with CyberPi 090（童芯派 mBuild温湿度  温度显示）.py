""""
名称：090 童芯派 mBuild温湿度 温度显示
硬件： 童芯派 mBuild点阵屏、温湿度传感器
功能介绍：
将温湿度传感器的读值显示在LED点阵屏上。


使用到的API及功能解读：
1.cyberpi.humiture.get_humidity()
获取温湿度传感器的湿度读值

2.cyberpi.humiture.get_temp()
获取温湿度传感器的温度读值

3.cyberpi.led_matrix.print(str)
在LED点阵屏上显示文字，仅支持英文字母和数字。

难度：⭐⭐⭐
支持的模式：上传模式、在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time


while True:
    hum = cyberpi.humiture.get_humidity()
    cyberpi.led_matrix.print('H:' + str(hum))
    time.sleep(1)
    cyberpi.led_matrix.clear(1)
    temp = cyberpi.humiture.get_temp()
    cyberpi.led_matrix.print('T:' + str(temp))
    time.sleep(1)
    cyberpi.led_matrix.clear(1)
