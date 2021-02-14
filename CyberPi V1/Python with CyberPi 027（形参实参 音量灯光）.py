""""
名称：027 函数 形参与实参 音量灯光
硬件： 童芯派
功能介绍：定义灯光函数，通过获取声音传感器的读值传递灯光函数中，实现对灯光的控制。

难度：⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.函数
  定义函数需要使用到python中的关键字 def
  def 函数名称()：         在函数名称的括号内可以设置多个参数，这个参数叫做形式参数，也称为形参
      函数内的功能             在封装的功能中会对形参进行调用。
  举例：
      def plus(a):       定义函数plus(a),形式参数为啊
          print(a+1)          在控制台上打印（a + 1）的值

      b = 3              设置变量的值为3
      plus(b)            调用函数plus，在这里参数是b,这里参数b也被称为实际参数。
                         目的就是将参数b的值传递给形式参数a,然后函数根据封装的功能进行执行。
                         b = 3,传递参数后形式参数a = 3,print(a + 1),则等于print(3 + 1)
                         故会在控制台上输出4。

2.cyberpi.barchart.add(data)
  童芯派的柱状图，显示(数据)   用于在屏幕上显示柱状图，data参数填入柱状图的参数

3.cyberpi.display.set_brush(r, g, b)
  童芯派的屏幕显示内容的颜色，r,g,b值填入对应的r, g, b值。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi  # 导入童芯派的第三方库


def soundlight(sound):                          # 定义函数soundlight，形参sound
    sound = sound * 0.255                       # 将音量的值映射到RGB值的区间
    sound = int(sound)                          # 利用int函数对sound的值进行取整
    cyberpi.led.on(sound, sound, sound, "all")  # 点亮童芯派的灯光


cyberpi.display.clear()                         # 清空童芯派的屏幕，进行初始化
while True:                                     # 重复执行
    loud = cyberpi.get_loudness()               # 将声音传感器获得的数值赋值给变量loud
    cyberpi.display.set_brush(0, 255, 0)        # 设置屏幕显示的颜色为绿色
    cyberpi.barchart.add(loud)                  # 根据loud的数值生成柱状图
    soundlight(loud)                            # 调用函数soundlight(sound)



