""""
名称：024 For循环（2）随机灯光颜色
硬件：童芯派
功能介绍：通过For循环实现灯光的循环点亮。

难度：⭐⭐⭐

支持的模式：在线 上传

使用功能解读：
1. range函数
   range(begin, stop, step)
   range函数可以生成一个有序的数列，begin表示数列的起始值，stop表示结束值，
step表示步长。
   举个例子：range(1, 10, 1)
   表示利用range函数生成一个，起始值为1，结束值为10的参数，数值差为1的数列。
   其中需要注意的是，这个数值是不包含结束值本身的。
   通过print(list(range(1, 10, 1)))可以得到以下数列
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   如果将step参数修改为2，则得到的数列如下：
   [1 ,3, 5, 7, 9]

2. for i in range(1, 10, 1)
   i会随着range函数生成的数值变化而变化。
   即随着循环，i的数值会从1-9进行变化，跟上面生成的列表一样。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import random
import time

cyberpi.console.clear()
cyberpi.led.off()  # 熄灭童心派的灯光进行初始化
for i in range(1, 6, 1):  # for循环，起始值为1，结束值为6，步长为1：(也就是循环5次)
    cyberpi.console.println(i)
    r = random.randint(0, 255)  # 生成随机颜色的rgb值
    g = random.randint(0, 255)  # 生成随机颜色的rgb值
    b = random.randint(0, 255)  # 生成随机颜色的rgb值
    cyberpi.led.on(r, g, b, i)  # 童心派根据生成的随机值，点亮第i个灯光
    time.sleep(0.5)  # 等待0.5秒
    cyberpi.led.off()  # 熄灭灯光

# 拓展
# 尝试修改使用range函数，设置不同的起始值和结束值，以及步长，
# 在童心派的屏幕上进行数值的输出。
