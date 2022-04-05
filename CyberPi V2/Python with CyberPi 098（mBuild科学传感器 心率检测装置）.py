""""
名称：098 童芯派 mBuild科学传感器 心率检测仪
硬件： 童芯派 mBuild科学传感器
结合童芯派和mBuild科学传感器上的心率传感器设计一个心率检测仪。
同时童芯派的屏幕可以显示历史检测数据。

使用到的API及功能解读：

1.cyberpi.science.heart_on(1)
切换心率传感器为工作状态为打开

2.cyberpi.science.heart_is_finish(1)
返回心率传感器的检测状态

3.cyberpi.science.heart_get(1)
获取心率传感器检测结果

4.cyberpi.science.heart_off(1)
切换心率传感器工作状态为关闭

难度：⭐⭐⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
import random



def heartbeat ():
    cyberpi.science.heart_on(1)
    cyberpi.led.show('red black black black black')
    cyberpi.display.show_label('心率测量中', 16, "center", index=0)
    while not cyberpi.science.heart_is_finish(1):
        cyberpi.led.move(1)
        time.sleep(0.1)
    result = cyberpi.science.heart_get(1)
    cyberpi.science.heart_off(1)
    cyberpi.led.off("all")
    cyberpi.console.clear()
    return result

def basic ():
    cyberpi.console.clear()
    cyberpi.display.set_brush(0, 0, 255)
    cyberpi.console.println('摇杆中间键检测心率')
    cyberpi.console.println('上、下键显示数据 ')
    cyberpi.console.println('B键回到此界面')



count = 0
beat_list = []
cyberpi.wifi.connect('Maker-guest', 'makeblock')
while not cyberpi.wifi.is_connect():
    pass
cyberpi.display.set_brush(0, 0, 255)
cyberpi.display.show_label('童芯智慧医疗', 16, "center", index=0)
time.sleep(3)
cyberpi.console.clear()
cyberpi.display.show_label('童芯心率检测仪', 16, "center", index=0)
time.sleep(1)
basic()

while True:
    if cyberpi.controller.is_press('b'):
        basic()
    if cyberpi.controller.is_press('middle'):
        cyberpi.console.clear()
        cyberpi.display.set_brush(255, 0, 0)
        cyberpi.console.println('请将手指放置在心率传感器上')
        cyberpi.console.println('3秒后开始心率测量')
        time.sleep(3)
        cyberpi.console.clear()
        cyberpi.audio.play('prompt-tone')
        beat = heartbeat()
        cyberpi.audio.play('prompt-tone')
        cyberpi.console.println('测量结果' + str(beat) + '/min')
        cyberpi.console.println('是否存储本次测量数据？（按下A键确认，B键放弃）')
        while True:
            if cyberpi.controller.is_press('a'):
                beat_list.append(beat)
                basic()
                break
            elif cyberpi.controller.is_press('b'):
                basic()
                break
    if cyberpi.controller.is_press('up'):
        cyberpi.console.clear()
        cyberpi.display.set_brush(0, 255, 0)
        cyberpi.linechart.set_step(5)
        count = 1
        if len(beat_list) < 2:
            cyberpi.display.show_label('数据量不足', 16, "center", index=0)
        else:
            while not count > len(beat_list):
                cyberpi.linechart.add(beat_list[count - 1] * 0.8)
                count = count + 1
                time.sleep(0.2)
    if cyberpi.controller.is_press('down'):
        cyberpi.console.clear()
        count = 1
        if len(beat_list) == 0:
            cyberpi.display.show_label('数据量不足', 16, "center", index=0)
            pass
        else:
            while not count > len(beat_list):
                cyberpi.display.set_brush(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                cyberpi.barchart.add(beat_list[count - 1] * 0.8)
                count = count + 1
                time.sleep(0.2)   