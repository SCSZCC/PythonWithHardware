""""
名称：055 掌上扩展板-电机控制
硬件： 童芯派 + 掌上扩展板 + 电机
功能介绍：
利用掌上扩展板驱动电机，实现对电机的控制

难度：⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.cyberpi.pocket.xxxx
通过调用cyberpi的pocket模块，可以调用童芯派的掌上扩展板的功能。
掌上扩展板可以给童芯派提供电力和更强的电压，以实现童芯派对电机、
舵机、灯带及其它第三方传感器的使用。

2.cyberpi.pocket.motor_set(power, port)
用以控制指定接口的电机的动力控制，power取值0-100，port为接口名称。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time


cyberpi.pocket.motor_stop('m1')
while True:
    if cyberpi.controller.is_press("a"):
        cyberpi.pocket.motor_set(100,'m1')
        time.sleep(0.3)
    if cyberpi.controller.is_press('b'):
        cyberpi.pocket.motor_stop('m1')
        time.sleep(0.3)