""""
名称：019 按键录音机
硬件：童芯派
功能介绍：通过童芯派上的按键控制灯光的亮灭

难度：⭐⭐

支持的模式：在线 上传

使用功能解读：
1. cyberpi.controller.is_press("button")
   童芯派.按键.按下("按钮名称")
   button 可以填入 "a" "b" "up" "down" "left" "right" "middle"
   分别代表同童芯派的a b键，和摇杆的上下左右中键
   返回值数值类型为布尔型 。按键按下返回值为True，否则返回值为False

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.console.println("按下A键开始录音")
while True:                                          # while True 重复执行：
    if cyberpi.controller.is_press("a"):                 # 如果童芯派按键A按下：
        cyberpi.audio.record()                                # 童芯派开始录音
        cyberpi.console.println("开始录音")                     # 屏幕显示文字”开始录音“
        time.sleep(0.3)                                       # 设置等待0.3秒，避免循环过快
    if cyberpi.controller.is_press("b"):                 # 如果童芯派按键B按下：
        cyberpi.audio.stop_record()                           # 童芯派停止录音
        cyberpi.console.println("停止录音")                     # 屏幕显示文字”停止录音“
        time.sleep(0.3)                                       # 设置等待0.3秒，避免循环过快，反复触发
    if cyberpi.controller.is_press("middle"):            # 如果童芯派摇杆的中间被按下：
        time.sleep(0.3)                                       # 等待0.3秒
        cyberpi.console.println("开始播放录音")                 # 童芯派屏幕显示文字开始播放录音
        cyberpi.audio.play_record()                           # 童芯派开始播放录音。