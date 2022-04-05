""""
名称：073 童芯派 童芯派鼠标
硬件： 童芯派
功能介绍：
利用童芯派的陀螺仪模块和按键结合pynput模块的鼠标控制功能，实现鼠标的功能。
通过陀螺仪控制鼠标移动。通过按键实现鼠标按键功能。
结合蓝牙模块可以实现无线鼠标的功能。



难度：⭐⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
from pynput.mouse import Button, Controller
import cyberpi
import time

mouse = Controller()

while True:
    if cyberpi.is_tiltback():
        mouse.move(-3, 0)
        print(mouse.position)
    if cyberpi.is_tiltforward():
        mouse.move(3, 0)
    if cyberpi.is_tiltleft():
        mouse.move(0, -3)
    if cyberpi.is_tiltright():
        mouse.move(0, 3)
    if cyberpi.controller.is_press("b"):
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.press(Button.left)
        mouse.release(Button.left)
    if cyberpi.controller.is_press("a"):
        mouse.press(Button.right)
        mouse.release(Button.right)
    time.sleep(0.01)



