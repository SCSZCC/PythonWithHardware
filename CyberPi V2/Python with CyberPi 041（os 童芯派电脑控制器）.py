""""
名称：041 童芯电脑控制器
硬件： 童芯派
功能介绍：用童芯派控制电脑软件的打开。


难度：⭐⭐⭐

支持的模式：仅支持在线模式

使用到的API及功能解读：
1.os库
os是Python的内建库，不需要单独进行安装就可以进行调用。可以用于路径操作、进程管理等功能

2.import os
导入os模块

3.os.startfile()
用于打开外部程序或文件。括号内填入文件的路径位置。在路径前面可以增加一个r，表示只读模式。
示例：
os.startfile(r"文件路径名")


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import os
import time

while True:
    if cyberpi.controller.is_press("a"):
        cyberpi.console.println("正在打开音乐软件")
        os.startfile(r"D:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe")
        time.sleep(1)
    elif cyberpi.controller.is_press("b"):
        cyberpi.console.println("灯光已打开")
        cyberpi.led.on(255, 255, 255)
