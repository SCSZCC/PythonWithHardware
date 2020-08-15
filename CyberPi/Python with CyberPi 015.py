""""
名称：015 想亮哪里亮哪里
硬件：童芯派
功能介绍：通过输入信息，控制童芯派灯光的颜色

难度：⭐⭐

支持的模式：在线

使用功能解读：
1. 双分支结构
if-条件1  :
----条件成立执行的代码
elif-条件2
----条件2成立时执行的代码
elif-条件3
----条件3成立时执行的代码
else:
----条件1 2 3 都不成立时执行的代码

在多分支结构当中，可以增设多个elif语句在里面。

- 表示空格
条件成立，返回值则为True，条件不成立则返回值False


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi

cyberpi.led.off()                                         # 熄灭所有LED灯，进行灯光初始化
led_num = int(input("请输入制定的LED的位置（1-5）: "))        # 输入要打开的LED灯位置序号
if led_num == 1:                                          # 用if判断light_num中的数据是否为1
    cyberpi.led.on(255, 255, 255, 1)                          # 条件成立则打开第1个LED灯
elif led_num == 2:                                        # 否则判断light_num中的数据是否为2
    cyberpi.led.on(255, 255, 255, 2)                          # 条件成立则打开第2个LED灯
elif led_num == 3:                                        # 否则判断light_num中的数据是否为3
    cyberpi.led.on(255, 255, 255, 3)                          # 条件成立则打开第3个LED灯
elif led_num == 4:                                        # 否则判断light_num中的数据是否为4
    cyberpi.led.on(255, 255, 255, 4)                          # 条件成立则打开第4个LED灯
elif led_num == 5:                                        # 否则判断light_num中的数据是否为5
    cyberpi.led.on(255, 255, 255, 5)                          # 条件成立则打开第5个LED灯
else:                                                     # 否则
    cyberpi.led.off()                                         # 灯光保持关闭


# 拓展
#    1.你可以用数字来控制童芯派播放制定的音效吗？
