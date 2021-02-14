""""
名称：076 童芯派 mBot2启动
硬件： 童芯派
功能介绍：
给基于童芯派的mBot2编写一个灯光启动灯效，涉及到超声波与四路巡线传感器灯光控制。
程序当中使用了两个四路巡线传感器。


难度：⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi

cyberpi.audio.set_vol(100)
cyberpi.audio.play_until('spitfire')
for i in range(0, 256, 25):
    if i>=255:
        i = 255
    cyberpi.led.on(i, 0, 0)
    cyberpi.ultrasonic2.set_bri(i)
cyberpi.quad_rgb_sensor.set_led("blue", 1)
cyberpi.quad_rgb_sensor.set_led("red", 2)
while not cyberpi.controller.is_press('a'):
    cyberpi.quad_rgb_sensor.set_led("blue", 1)
    cyberpi.quad_rgb_sensor.set_led("red", 1)
    cyberpi.led.on('r')
    time.sleep(0.2)
    cyberpi.quad_rgb_sensor.off_led(1)
    cyberpi.quad_rgb_sensor.off_led(2)
    cyberpi.led.off()