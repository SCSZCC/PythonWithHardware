""""
名称：003 声音播放器
硬件：
功能介绍：让童芯派播放音乐
难度：⭐
支持的模式：上传、在线都支持

使用到的API及功能解读：
1.cyberpi.audio.play_until('hello')
  童芯派的.音效.播放预置音效到结束（'hello'）
  更多音效名称请查阅童芯派API文档
2.cyberpi.audio.play_music(note, beat, type='piano')
  童芯派的.音效.播放乐器音效（音调，节拍，乐器类型为：钢琴）
  使用示例：cyberpi.audio.play_music(67, 0.25, 'piano')
"""

# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi  # 导入童芯派的第三方库

cyberpi.audio.play_until("hello")
cyberpi.audio.play_music(60, 0.25, 'piano')
cyberpi.audio.play_music(60, 0.25, 'piano')
cyberpi.audio.play_music(67, 0.25, 'piano')
cyberpi.audio.play_music(67, 0.25, 'piano')
cyberpi.audio.play_music(69, 0.25, 'piano')
cyberpi.audio.play_music(69, 0.25, 'piano')
cyberpi.audio.play_music(67, 0.5, 'piano')

# 拓展：
# 1.你可以将根据以下的音调完成小星星的程序编写吗？
# 60 60 67 67 69 69 67  65 65 64 64 62 62 60    67 67 65 65 64 64 62
# 67 67 65 65 64 64 62  60 60 67 67 69 69 67    65 65 64 64 62 62 60
# 每小节最后一个音符为0.5拍
# 2.如果将cyberpi.audio.play_until('hello')更换成 cyberpi.audio.play('hello')效果有什么变化？

