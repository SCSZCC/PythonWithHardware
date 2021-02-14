""""
名称：082 童芯派 mBot2光感灯光系统
硬件： 童芯派
功能介绍：
使用童芯派上的光线传感器控制新超声波上的LED灯。模仿汽车前灯。

使用到的API及功能解读：
1.cyberpi.get_bri()
获得童芯派光线传感器的读值
返回数值，可能的范围为0-100。



难度：⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi


while True:
    if cyberpi.get_bri() < 20:
        cyberpi.ultrasonic2.set_bri(100, "all", 1)
        cyberpi.led.show('r r k r r')
    else:
        cyberpi.ultrasonic2.set_bri(0, "all", 1)
        cyberpi.led.off()


