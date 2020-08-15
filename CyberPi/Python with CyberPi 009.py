""""
名称：009 全屏文本显示（1）
硬件：童芯派
功能介绍：实现童芯派全屏文本的显示

难度：⭐⭐

支持的模式：在线

使用功能解读：
1.cyberpi.display.show_label(message, size, x, y)
  童芯派.显示.全屏文本（显示的内容， 文字大小， 起始点屏幕中的x坐标， 屏幕中的y坐标）
        message参数用于表示要在屏幕上显示的信息
        size参数：表示文字大小，有16，24，32，三种大小的字号可以选择
        x参数，表示文字在屏幕中的X轴坐标，取值范围为0-128
        y参数，表示文字在屏幕中的Y轴坐标，取值范围为0-128

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.display.clear()                            # 清空屏幕
cyberpi.display.show_label("你好", 24, 50, 50)      # 显示你好在坐标（50，50）的位置
time.sleep(0.5)                                    # 等待0.5秒
cyberpi.display.clear()                            # 清空屏幕
cyberpi.display.show_label("你好", 24, 100, 100)    # 显示你好在坐标（100，100）的位置（在这个位置显示不全）
time.sleep(0.5)                                    # 等待0.5秒
cyberpi.display.clear()                            # 清空屏幕
cyberpi.display.show_label("你好", 24, 0, 0)        # 显示你好在坐标（0，0）的位置
time.sleep(0.5)                                    # 等待0.5秒
cyberpi.display.clear()                            # 清空屏幕
cyberpi.display.show_label("你好", 24, 128, 128)    # 显示你好在坐标（128，128）的位置(实际已经看不到了)
time.sleep(0.5)

