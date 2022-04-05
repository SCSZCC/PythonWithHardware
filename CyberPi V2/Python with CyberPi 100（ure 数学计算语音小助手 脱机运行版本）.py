""""
名称：100 童芯派 ure 数学计算语音小助手 脱机运行版本
硬件： 童芯派
使用童芯派的语音识别功能，MicroPython的ure模块对识别的结果进行处理。
实现提问数学计算题，并得出结果的功能。
但是只能实现两个整数之间的加减乘除运算。
这个程序仅支持离线模式进行运行。

使用到的API及功能解读：

1.import ure
导入ure模块

2.get = ure.match('(\d+)(乘以|加|减|除以)(\d+)',result[0:-1])
根据定义的正则表达式对识别结果的数据进行处理。()的作用是对字符串进行分组。
并将结果存放在变量get当中。

3.get.group(1)
获取get变量当中指定分组的数据

难度：⭐⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
import random
import ure


c=0
cyberpi.cloud.setkey("请输入云服务授权码")
cyberpi.console.clear()
cyberpi.console.println("童芯派启动成功！")
cyberpi.wifi.connect("WiFi名称", "WiFi密码")
cyberpi.console.println("WIFI连接中...")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.led.on(0, 0, 255)
cyberpi.console.clear()
cyberpi.display.show_label("WiFi连接成功", 16, "center", index=0)
time.sleep(1)


while True:
    if cyberpi.controller.is_press("a"):
        cyberpi.console.clear()
        cyberpi.console.println("开始语音识别")
        cyberpi.led.on(0, 255, 0)
        cyberpi.cloud.listen("chinese", 2)
        result = cyberpi.cloud.listen_result()
        cyberpi.console.println(result)
        try:    
            get = ure.match('(\d+)(乘以|加|减|除以)(\d+)',result[0:-1])
            a = int(get.group(1))
            b = int(get.group(3))
            calculate = get.group(2)
            if '乘以' in calculate:
                c = a * b
            elif '除以' in calculate:
                c = a / b
            elif '加' in calculate:
                c = a + b
            elif '减' in calculate:
                c = a - b
            cyberpi.console.println('答案为'+str(c))
            cyberpi.cloud.tts("zh", '答案为'+str(c))
        except BaseException:
            cyberpi.console.println('数据不足或超出计算能力范围，请重新按下A键')
            cyberpi.cloud.tts("zh", "数据不足或超出计算能力范围,请重新按下A键")
            

        
