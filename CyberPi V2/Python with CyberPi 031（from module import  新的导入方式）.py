"""
名称：031 from module import * 新的导入方式
硬件： 童芯派
功能介绍：换一种方式导入cyberpi库，以后看到类似的情况，可不要觉得太陌生。

难度：⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：

from module import *
示例：
from cyberpi import *
将所有的cyberpi的所有模块功能进行导入。在调用的时就可以直接使用模块功能，不需要使用模块名。

比如使用led功能。
import cyberpi模式下调用灯光api的方式是：cyberpi.led.on(255, 255, 255)
from cyberpi import *下调用灯光api的方式是：led.on(255, 255, 255)

建议在使用单一模块的情况下，使用from module import *的形式，如果在多个模块下使用，
可能会产生冲突。
童芯派的from cyberpi import * 的调用方式会更适合使用在上传模式下。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

from cyberpi import *                 # 导入cyberpi的所有功能

while True:                           # 重复执行
    if controller.is_press("a"):          # 如果按键a被按下：
        led.on(255, 255, 255)                 # 打开LED灯光
    if controller.is_press("b"):          # 如果按键b被按下：
        led.off()                             # 关闭LED灯光



