""""
名称：016 循环的小星星
硬件：童芯派
功能介绍：通过循环语句，播放部分小星星的音乐片段

难度：⭐⭐

支持的模式：在线、上传

使用功能解读：
1. while循环结构：

while-条件成立:
----条件成立执行的代码

- 表示空格
条件成立，返回值则为True，条件不成立则返回值False
无限循环可以将条件设为True，即
while True:
   循环重复执行的代码

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.audio.set_vol(100)                           # 设置播放音量为50%
cyberpi.audio.set_tempo(50)                          # 设置播放速度为0.5倍速，即50%
while True:                                          # while True 重复执行：
    cyberpi.audio.play_music(60, 0.25, 'piano')          # 需要重复执行的音效代码
    cyberpi.audio.play_music(60, 0.25, 'piano')
    cyberpi.audio.play_music(67, 0.25, 'piano')
    cyberpi.audio.play_music(67, 0.25, 'piano')
    cyberpi.audio.play_music(69, 0.25, 'piano')
    cyberpi.audio.play_music(69, 0.25, 'piano')
    cyberpi.audio.play_music(67, 0.5, 'piano')
    cyberpi.audio.play_music(65, 0.25, 'piano')
    cyberpi.audio.play_music(65, 0.25, 'piano')
    cyberpi.audio.play_music(64, 0.25, 'piano')
    cyberpi.audio.play_music(64, 0.25, 'piano')
    cyberpi.audio.play_music(62, 0.25, 'piano')
    cyberpi.audio.play_music(62, 0.25, 'piano')
    cyberpi.audio.play_music(60, 0.5, 'piano')
    time.sleep(1)


# 拓展
#    1.你可以让童芯派上的5个LED灯循环单独点亮吗？

