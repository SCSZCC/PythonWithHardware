""""
名称：022 循环的终止
硬件：童芯派
功能介绍：通过while循环的条件控制循环的结束。

难度：⭐⭐

支持的模式：在线 上传

使用功能解读：
1. while condition:
      条件（condition）满足执行的代码

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi

cyberpi.display.clear()
cyberpi.console.println("灯光已打开")         # 屏幕显示灯光已打开
while cyberpi.get_loudness() <= 50:         # 重复执行直到 童芯派侦测到的音量小于50不成立 ：
    cyberpi.led.on(255, 255, 255)           #     灯光打开
cyberpi.console.println("灯光已关闭")         # 屏幕显示灯光已关闭（while循环已结束）
cyberpi.led.off()                           # 关闭童芯派的灯光。

