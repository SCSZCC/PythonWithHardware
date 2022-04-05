""""
名称：030 阶段一综合应用
硬件： 童芯派
功能介绍：在童芯派上制作一个倒计时功能，可以自定义倒计时的时间。

难度：⭐⭐⭐⭐⭐

支持的模式：上传、在线都支持

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi  # 导入童芯派的第三方库
import time


def countdown(hour, minute, second):
    while True:
        if hour == 0 and minute == 0 and second == 0 or cyberpi.controller.is_press("b"):
            cyberpi.display.show_label("倒计时结束", 24, "center", index=0)
            cyberpi.audio.play("beeps")
            time.sleep(3)
            return False
        if second == 0:
            minute -= 1
            second = 59
            if minute < 0:
                hour -= 1
                minute = 59
                if hour < 0:
                    hour = 0
        second -= 1
        cyberpi.display.show_label(str(hour) + ":" + str(minute) + ":" + str(second), 32, "center",index=0)
        time.sleep(1)


h = 0
m = 0
s = 0
begin = False
cyberpi.console.clear()
cyberpi.console.println("摇杆上下增减秒数")
cyberpi.console.println("摇杆左右增减分数")
cyberpi.console.println("摇杆中间增加小时")
time.sleep(5)
cyberpi.console.clear()
while True:
    cyberpi.display.show_label(str(h) + ":" + str(m) + ":" + str(s), 16, "center", index=0)
    if cyberpi.controller.is_press('up'):
        s += 1
        if s == 60:
            s = 0
    if cyberpi.controller.is_press('down'):
        s -= 1
        if s < 1:
            s = 0
    if cyberpi.controller.is_press("left"):
        m -= 1
        if m < 1:
            m = 0
    if cyberpi.controller.is_press("right"):
        m += 1
        if m == 60:
            mi = 0
    if cyberpi.controller.is_press("middle"):
        h += 1
    if cyberpi.controller.is_press("a"):
        cyberpi.display.show_label(str(h)+":"+str(m)+":"+ str(s), 24, "center", index=0)
        cyberpi.audio.play("beeps")
        begin = True
        countdown(h, m, s)
    time.sleep(0.1)
