""""
名称：004 声音播放器-变调
硬件：童芯派
功能介绍：让童芯派换个声音

难度：⭐

支持的模式：上传、在线

使用到的API及功能解读：
1.cyberpi.audio.set_vol(pct)
  童芯派的.音效.设置音量大小为（pct）    pct参数的数值范围 0-100。表示音量大小的百分比。
  使用示例：cyberpi.audio.set_tempo(200)

2.cyberpi.audio.set_tempo(pct)
  童芯派的.音效.设置播放速度（pct）     pct参数的数值范围25-400。表示播放速度的百分比。
  使用示例：cyberpi.audio.set_tempo(50)

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi

cyberpi.audio.set_vol(50)  # 设置播放音量为50%
cyberpi.audio.set_tempo(200)  # 设置播放速度为2倍速，即200%
cyberpi.audio.play_until("hello")
cyberpi.audio.play_music(60, 0.25, 'piano')
cyberpi.audio.play_music(60, 0.25, 'piano')
cyberpi.audio.play_music(67, 0.25, 'piano')
cyberpi.audio.play_music(67, 0.25, 'piano')
cyberpi.audio.play_music(69, 0.25, 'piano')
cyberpi.audio.play_music(69, 0.25, 'piano')
cyberpi.audio.play_music(67, 0.5, 'piano')
