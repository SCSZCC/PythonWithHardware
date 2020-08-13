""""
名称：002 屏幕上的文字
硬件：
功能介绍：在童芯派的屏幕上显示文字

难度：⭐

支持的模式：上传、在线

使用到的API及功能解读：
1.cyberpi.console.print('char')
  童芯派的.控制台（屏幕）.打印文字（'要打印的文字内容'）

2.cyberpi.display.clear()
  童芯派的.显示.清空（）

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi                                  # 导入童芯派的第三方库

cyberpi.display.clear()                         # 清空屏幕上的内容，对屏幕进行初始化
cyberpi.console.print('一起来学Python吧！')       # 在屏幕上打印显示  一起来学Python吧！
cyberpi.console.print('加油！')                  # 在屏幕上打印显示：“加油”！




# 拓展：
#    1.将代码中的print更换成println，观察效果上的变化。
#    2.如果删除cyberpi.display.clear(),再次运行程序，观察屏幕的显示变化。

