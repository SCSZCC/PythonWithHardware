""""
名称：081 童芯派 mBot2超声波避障
硬件： 童芯派
功能介绍：
结合mBot2的新超声波模块实现避障功能。

使用到的API及功能解读：
1.cyberpi.ultrasonic2.get()
获得新超声波传感器与障碍物之间的距离。
返回数值，可能的范围为3 - 300，单位是cm，误差为±5%。



难度：⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi


while True:
    if cyberpi.ultrasonic2.get() <= 50:
        cyberpi.led.on(255,0,0)
        cyberpi.mbot2.drive_power(0, 0)
    else:
        cyberpi.led.off()
        cyberpi.mbot2.drive_power(50, 50)


