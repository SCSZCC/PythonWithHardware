""""
名称：032 童芯派柱状图生成
硬件： 童芯派
功能介绍：使用童芯派屏幕显示柱状图

难度：⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.cyberpi.barchart.add(data)
  生成单一柱形图，data参数填入要生成的数据。如果要生成多组数据，
  需要配合cyberpi.display.set_brush(r, g, b)
  一种颜色生成条柱形。

2.cyberpi.display.set_brush(r, g, b)
  设置屏幕效果的颜色。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi


def light():
    sound = cyberpi.get_loudness()
    cyberpi.barchart.add(sound)
    sound = sound * 2.55
    cyberpi.led.on(sound, sound, sound)


cyberpi.display.clear()
while True:
    cyberpi.display.set_brush(255, 0, 0)
    light()
    cyberpi.display.set_brush(0, 255, 0)
    light()
    cyberpi.display.set_brush(0, 0, 255)
    light()
    cyberpi.display.set_brush(255, 255, 0)
    light()
    cyberpi.display.set_brush(0, 255, 255)
    light()
