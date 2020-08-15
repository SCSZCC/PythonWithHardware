""""
名称：018 按键灯
硬件：童芯派
功能介绍：通过童芯派上的按键控制灯光的亮灭

难度：⭐⭐

支持的模式：在线 上传

使用功能解读：
1. cyberpi.controller.is_press("button")
   童芯派.按键.按下("按钮名称")
   button 可以填入 "a" "b" "up" "down" "left" "right" "center"
   分别代表同童芯派的a b键，和摇杆的上下左右中键
   返回值数值类型为布尔型 。按键按下返回值为True，否则返回值为False


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi


while True:                                          # while True 重复执行：
    if cyberpi.controller.is_press("a"):                 # 如果童芯派按键A按下：
        cyberpi.led.on(255, 255, 255)                        # 打开童芯派的灯光
    if cyberpi.controller.is_press("b")                  # 如果童芯派按键B按下：
        cyberpi.led.off()                                    # 关闭童芯派的灯光

# 拓展
#    1.相信你也可以实现一个AB按键实现不同音效的播放。




