""""
名称：080 童芯派 mBot2多路巡线 基于偏移量巡线
硬件： 童芯派
功能介绍：
使用mBot2的四路巡线传感器实现，通过四路传感器检测到的偏移量来实现巡线功能。
通过偏移量与系数kp实现巡线的功能。

使用到的API及功能解读：
1.cyberpi.quad_rgb_sensor.get_offset_track(1)
表示四路颜色传感器检测到巡线的线偏移程度，可能值为 -100~100。-100 时，
四路颜色传感器位于巡线的左侧。1表示四路巡线传感器的序号。
如果小车当中没有使用多个四路巡线传感器，则该参数可以默认不用填写。



难度：⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time


kp = 0.6
base_power = 55
while cyberpi.controller.is_press("a") == False:
    pass
while True:
    right_power = -1 * (base_power +kp * cyberpi.quad_rgb_sensor.get_offset_track(1))
    left_power = base_power - (kp * cyberpi.quad_rgb_sensor.get_offset_track(1))
    cyberpi.mbot2.drive_power(left_power, right_power)
    if cyberpi.controller.is_press("b"):
        while cyberpi.controller.is_press("a") == False:
            cyberpi.mbot2.drive_power(0, 0)    
        time.sleep(0.5)


