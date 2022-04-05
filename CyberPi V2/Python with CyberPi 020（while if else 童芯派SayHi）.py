""""
名称：020 Say Hi
硬件：童芯派
功能介绍：通过童芯派上的按键控制灯光的亮灭

难度：⭐⭐

支持的模式：在线 上传

使用功能解读：
1. cyberpi.audio.play_until("audio_name")
   童芯派.音效.播放直到音效结束("音效名称")
   audio_name参数填写音效名称。

2. cyberpi.audio.stop()
   童芯派.音效.停止播放


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi

cyberpi.display.clear()                              # 清空屏幕，进行初始化。
cyberpi.console.println("跟我Say Hi吧")                 # 屏幕显示提示语
while True:                                          # while True 重复执行：
    if cyberpi.get_loudness() >= 80:                     # 如果童芯派侦测到的声音大小大于80：
        cyberpi.audio.play_until("hi")                       # 那么播放完音效hi
    else:                                                # 否则
        cyberpi.audio.stop()                                 # 停止音效的播放