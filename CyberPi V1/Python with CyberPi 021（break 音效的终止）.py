""""
名称：021 音效的终止
硬件：童芯派
功能介绍：通过条件语句和break关键字结束音效的播放。

难度：⭐⭐

支持的模式：在线 上传

使用功能解读：
1. cyberpi.audio.play_drum("bass-drum", 0.25)
   童芯派.音效.架子鼓(“type”,beat)
   tpye处填入音效类型，beat参数填入节拍，0.25拍约等于0.25秒

2.break
  结束
  一般与if语句一起使用，用于跳出当前所在的循环。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi

cyberpi.display.clear()
cyberpi.audio.set_vol(100)
while True:                                         # 重复循环
    if cyberpi.controller.is_press("a"):                # 如果童芯派按键A按下：
        cyberpi.console.println("程序运行结束！")              # 屏幕显示程序运行结束。
        break                                                # 跳出当前所在的while循环
    else:                                           # 否则
        cyberpi.audio.play_drum("bass-drum", 0.25)      # 播放音效bass-drum 0.25拍
        cyberpi.audio.play_drum("bass-drum", 0.25)      # 播放音效bass-drum 0.25拍
        cyberpi.audio.play_drum("snare", 0.25)          # 播放音效snare 0.25拍