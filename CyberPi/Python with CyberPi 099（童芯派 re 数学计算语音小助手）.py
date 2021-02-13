""""
名称：099 童芯派 re 数学计算语音小助手
硬件： 童芯派
使用童芯派的语音识别功能，结合re正则表达式，对识别结果进行处理，
实现提问数学计算题，并得出结果的功能。
但是只能实现两个整数之间的加减乘除运算。
这个程序仅支持在线模式运行。

使用到的API及功能解读：

1.import re
正则表达式模块

2.get = re.findall("\d+", result)
获取变量result当中所有的数字，并转换成数值转换成列表。
并将结果存放在变量get当中。


难度：⭐⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
import random
import re


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
cyberpi.display.label("WiFi连接成功", 16, "center")
time.sleep(1)

while True:
    if cyberpi.controller.is_press("a"):
        cyberpi.console.clear()
        cyberpi.console.println("开始语音识别")
        cyberpi.led.on(0, 255, 0)
        cyberpi.cloud.listen("chinese", 2)
        result = cyberpi.cloud.listen_result()
        cyberpi.console.println(result)
        get = re.findall("\d+", result)
        if len(get)<2 or len(get)>=3:
            cyberpi.console.println('数据不足或超出计算能力范围，请重新按下A键')
            cyberpi.cloud.tts("chinese", "数据不足或超出计算能力范围,请重新按下A键")
            continue
        a = int(get[0])
        b = int(get[1])
        if '乘以' in result:
            c = a * b
        elif '除以' in result:
            c = a / b
        elif '加' in result:
            c = a + b
        elif '减' in result:
            c = a - b
        cyberpi.console.println('答案为'+str(c))
        cyberpi.cloud.tts("chinese", '答案为'+str(c))

        
