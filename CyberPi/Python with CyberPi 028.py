""""
名称：028 函数 返回值
硬件： 童芯派
功能介绍：了解函数返回值得使用方法，使用返回值作为条件，实现程序得判断。声控灯。

难度：⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.函数
  定义函数需要使用到python中的关键字 def
  def 函数名称()：
      函数内的功能             在封装的函数功能内，可以使用return关键词，实现返回值的功能
      return value           可以返回不同的数值，布尔值等

  举例：
      def plus(a):       定义函数plus(a),形式参数为啊
          return a + 3          在控制台上打印（a + 1）的值

      b = 3              设置变量b的值为3
      c = plus(b)        调用函数plus()，并设置实参b,
                         有b的数值传递给函数的形参a,故a等于3，函数的返回值为3+3，故返回值为6.
                         这里设置了变量c，因此返回的数值存放在变量c中，数值为6。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi  # 导入童芯派的第三方库
import random


def loud():                            # 定义函数loud
    if cyberpi.get_loudness() > 80:    # 判断获取的声音数值是否大于80，
        return False                       # 大于80，则返回值为False
    else:                              # 否则
        return True                        # 返回值为True


while loud():                          # 重复调用函数loud,如果返回值为True,则执行循环内的代码，否则结束循环。
    r = random.randint(0, 255)             # 定义r,g,b值得随机数
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cyberpi.led.on(r, g, b)                # 点亮随机颜色得灯光。

