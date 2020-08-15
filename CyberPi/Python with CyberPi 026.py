""""
名称：026 函数
硬件： 童芯派
功能介绍：依然还是小星星,不想要小星星？？？自己写啊。

难度：⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.函数
  定义函数需要使用到python中的关键字 def
  def 函数名称()：         def后面接函数的名称加一对括号和引号，表示无参数函数。
      函数内的功能          将功能代码编写在函数中，也被称之为封装。
  举例：
      def plus():
          print(1+1)
  例子中的函数名称叫plus,它封装的功能就是在控制台上打印1+1的值。
  如果在主程序中要调用函数的功能，只需要使用plus(),不需要def。
  plus()也被称为接口。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi  # 导入童芯派的第三方库


def section1():                                  # 定义函数section1
    cyberpi.console.println("section1")
    cyberpi.audio.play_music(60, 0.25, 'piano')
    cyberpi.audio.play_music(60, 0.25, 'piano')
    cyberpi.audio.play_music(67, 0.25, 'piano')
    cyberpi.audio.play_music(67, 0.25, 'piano')
    cyberpi.audio.play_music(69, 0.25, 'piano')
    cyberpi.audio.play_music(69, 0.25, 'piano')
    cyberpi.audio.play_music(67, 0.5, 'piano')


def section2():                                  # 定义函数section2
    cyberpi.console.println("section2")
    cyberpi.audio.play_music(65, 0.25, 'piano')
    cyberpi.audio.play_music(65, 0.25, 'piano')
    cyberpi.audio.play_music(64, 0.25, 'piano')
    cyberpi.audio.play_music(64, 0.25, 'piano')
    cyberpi.audio.play_music(62, 0.25, 'piano')
    cyberpi.audio.play_music(62, 0.25, 'piano')
    cyberpi.audio.play_music(60, 0.5, 'piano')


def section3():                                  # 定义函数section3
    cyberpi.console.println("section3")
    cyberpi.audio.play_music(67, 0.25, 'piano')
    cyberpi.audio.play_music(67, 0.25, 'piano')
    cyberpi.audio.play_music(65, 0.25, 'piano')
    cyberpi.audio.play_music(65, 0.25, 'piano')
    cyberpi.audio.play_music(64, 0.25, 'piano')
    cyberpi.audio.play_music(64, 0.25, 'piano')
    cyberpi.audio.play_music(62, 0.5, 'piano')


while True:                                      # 主程序  重复执行
    cyberpi.console.clear()
    section1()                                       # 调用函数section1
    section2()                                       # 调用函数section2
    section3()                                       # 调用函数section3
    section3()                                       # 调用函数section3
    section1()                                       # 调用函数section1
    section2()                                       # 调用函数section2

# 拓展：
# 1.也许你还可以在每段音乐的函数中封装灯光功能进去。
