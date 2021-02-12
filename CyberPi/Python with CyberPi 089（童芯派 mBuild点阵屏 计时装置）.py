""""
名称：089 童芯派 mBuild点阵屏 计时装置
硬件： 童芯派 mBuild点阵屏
功能介绍：
使用点阵屏实现可视化的计时效果,按下A键以点亮点阵屏的方式进行计时，
按下B键以熄灭点阵屏的方式进行计时。

使用到的API及功能解读：
1.cyberpi.led_matrix.on(x, y, 1)
点亮点阵屏指定x、y坐标的led灯

2.cyberpi.led_matrix.off(x, y, 1)
熄灭点阵屏指定x、y坐标的led灯

3.cyberpi.led_matrix.clear(1)
熄灭点阵屏所有的LED灯

难度：⭐⭐⭐⭐
支持的模式：上传模式、在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time


while True:
    cyberpi.display.label('按下A键开始计时', 16, 'center') 
    if cyberpi.controller.is_press('a'):
        cyberpi.display.label('计时中', 24, 'center') 
        for i in range(0, 8):
            for j in range(0, 16, 1):
                cyberpi.led_matrix.on(j, i, 1)
                time.sleep(1)
        cyberpi.led_matrix.clear(1)
        cyberpi.display.label('计时结束', '24', 'center')
        cyberpi.audio.play_until('prompt-tone')
    if cyberpi.controller.is_press('b'):
        cyberpi.display.label('计时中', 24, 'center') 
        for i in range(0, 8):
            for j in range(0, 16, 1):
                cyberpi.led_matrix.on(j, i, 1)
        for m in range(0, 8):
            for n in range(0, 16, 1):
                cyberpi.led_matrix.off(n, m, 1)
                time.sleep(1)
        cyberpi.display.label('计时结束', '24', 'center')
        cyberpi.audio.play_until('prompt-tone')