""""
名称：025 For循环（3）-呼吸灯
硬件：童芯派
功能介绍：利用for循环和while循环制作一个循环的呼吸灯灯效。

难度：⭐⭐⭐

支持的模式：在线 上传

使用功能解读：
1. 循环与循环直接是可以相互嵌套的，但是首先你需要自己梳理好循环之间的逻辑。

2. range函数也可以生成负数的数列。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

cyberpi.console.clear()
cyberpi.led.off()                     # 熄灭所有灯光进行初始化
while True:                           # 重复执行
    for i in range(0, 256, 51):       # for循环实现灯光的渐亮，i的数值随着循环增大。
        cyberpi.console.println(i)
        cyberpi.led.on(0, 0, i)             # 点亮led灯
        time.sleep(0.1)                     # 等待0.2秒
    for i in range(255, -1, -51):     # for循环实现灯光的歼灭，i的数值随着循环减小。
        cyberpi.console.println(i)
        cyberpi.led.on(0, 0, i)             # 点亮led灯
        time.sleep(0.1)                     # 等待0.2秒




# 拓展
# 尝试结合按键实现对灯光的渐亮和渐灭控制。

