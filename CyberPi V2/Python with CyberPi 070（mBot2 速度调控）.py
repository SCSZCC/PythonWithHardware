""""
名称：070 童芯派 智能小车 基础入门2
硬件： 童芯派 电机拓展板 编码电机
功能介绍：
利用按键控制mBot2的运行与停止，结合变量实现电机速度的控制

API：
1.设置mBot2左右编码电机的动力
 cyberpi.mbot2.drive_power(left_speed, right_speed)

难度：⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time


speed = 50
cyberpi.audio.set_vol(10)
while True:
    if cyberpi.controller.is_press('a'):
        cyberpi.audio.play_until('switch')
        cyberpi.mbot2.drive_power(speed, speed)
    if cyberpi.controller.is_press("b"):
        cyberpi.audio.play_until('switch')
        cyberpi.mbot2.drive_power(0, 0)
    if cyberpi.controller.is_press('up'):
        cyberpi.audio.play('level-up')
        speed += 10
        cyberpi.display.show_label("速度%s"%(speed), 24, 'center', index=0)
        time.sleep(0.2)
    if cyberpi.controller.is_press('down'):
        cyberpi.audio.play('level-up')
        speed -= 10
        cyberpi.display.show_label("速度%s"%(speed), 24, 'center', index=0)
        time.sleep(0.2)
