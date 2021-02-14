""""
名称：008 录音播放机
硬件：童芯派
功能介绍：实现童芯派5个LED灯的轮流点亮。

难度：⭐⭐⭐

支持的模式：在线

使用功能解读：
1.cyberpi.audio.record()
  童芯派开始录音,默认最长录音时长10秒

2.cyberpi.audio.stop_record()
  童芯派停止录音。

3.cyberpi.audio.play_record()
  童芯派播放录音内容。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.display.clear()                        # 清空屏幕
cyberpi.console.println("准备开始录音")          # 文字提示开始录音
cyberpi.console.println("3")                   # 显示倒计时3
time.sleep(1)                                  # 等待1秒
cyberpi.console.println("2")                   # 显示倒计时2
time.sleep(1)                                  # 等待1秒
cyberpi.console.println("1")                   # 显示倒计时1
time.sleep(1)                                  # 等待1秒
cyberpi.console.println("开始")                 # 提示开始录音
cyberpi.audio.record()                         # 童芯派开始录音
time.sleep(5)                                  # 等待5秒（帮助实现录音5秒的功能）
cyberpi.audio.stop_record()                    # 童芯派停止录音
cyberpi.console.println("录音结束，开始播放录音")  # 屏幕提示录音结束，并开始播放录音
cyberpi.audio.play_record()                    # 童芯派播放录音内容



# 拓展
#    1.在API文档当中了解
#            cyberpi.audio.play_record_until()
#            cyberpi.audio.play_record()
#            了解二者之间的区别