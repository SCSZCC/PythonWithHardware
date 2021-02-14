""""
名称：083 童芯派 mBot2 工作模式切换 蓝牙手柄
硬件： 童芯派 
功能介绍：
通过蓝牙手柄上的按键切换蓝牙mBot2的工作模式。
如自动化模式可以切换至自动巡线状态下，手动控制下可以通过蓝牙手柄控制mBot2


使用到的API及功能解读：
1.gamepad.is_key_pressed('Start')
表示蓝牙手柄上的'+'按键


难度：⭐⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time
import math
import gamepad
import mbot2


def line_follow(base_power, kp):
    right_power = -1 * (base_power +kp * cyberpi.quad_rgb_sensor.get_offset_track(1))
    left_power = base_power - (kp * cyberpi.quad_rgb_sensor.get_offset_track(1))
    cyberpi.mbot2.drive_power(left_power, right_power)


def remote_control():
    if not (math.fabs(gamepad.get_joystick('Ly'))<3 and math.fabs(gamepad.get_joystick('Ly'))<3):
        mbot2.drive_speed(((gamepad.get_joystick('Lx') + gamepad.get_joystick('Ly'))) / 2.55, ((gamepad.get_joystick('Lx') - gamepad.get_joystick('Ly'))) / 2.55)
    else:
        if gamepad.is_key_pressed('Up'):
            mbot2.forward(100)
            cyberpi.led.show('blue blue blue blue blue')
        else:
            if gamepad.is_key_pressed('Down'):
                mbot2.backward(100)
                cyberpi.led.show('red red red red red')
            else:
                if gamepad.is_key_pressed('Left'):
                    mbot2.turn_left(100)
                    cyberpi.led.show('yellow yellow black black black')
                else:
                    if gamepad.is_key_pressed('Right'):
                        mbot2.turn_right(100)
                        cyberpi.led.show('black black black yellow yellow')
                    else:
                        mbot2.EM_stop("ALL")
                        cyberpi.led.off("all")


status = 1
cyberpi.display.label("遥控模式", 24, 'center')
while True:
    if gamepad.is_key_pressed('Start'):
        status += 1
        time.sleep(1)
        if status == 2:
            cyberpi.display.label("巡线模式", 24, 'center')
        elif status >= 3:
            status = 1
            cyberpi.display.label("遥控模式", 24, 'center')
        cyberpi.audio.play_until('wake')
    if status == 1:
        remote_control()
    elif status == 2:
        line_follow(55, 0.6)
    





