""""
名称：079 童芯派 mBot2多路巡线 基于传感器状态
硬件： 童芯派
功能介绍：
使用mBot2的四路巡线传感器实现，基于传感器检测状态实现巡线功能。

使用到的API及功能解读：
1.cyberpi.quad_rgb_sensor.is_line("L1",1)  
判断指定位置的传感器是否检测到线段，'L1'表示传感器位置， 1表示四路巡线传感器的序号。
如果小车当中没有使用多个四路巡线传感器，则该参数可以默认不用填写。



难度：⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import mbuild

while True:
    if cyberpi.quad_rgb_sensor.is_line("L1",1) and cyberpi.quad_rgb_sensor.is_line("R1",1):
        cyberpi.mbot2.drive_power(40, 40)
    elif cyberpi.quad_rgb_sensor.is_line("L1",1) and cyberpi.quad_rgb_sensor.is_background("R1",1):
        cyberpi.mbot2.drive_power(0, 40)
    elif cyberpi.quad_rgb_sensor.is_background("L1", 1)  and cyberpi.quad_rgb_sensor.is_line("R1",1):
        cyberpi.mbot2.drive_power(40, 0)
