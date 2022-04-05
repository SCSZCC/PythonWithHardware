""""
名称：042 我和机器人的聊天记录
硬件： 童芯派
功能介绍：和机器人聊了很多内容，是不是可以像其它社交软件一样，能够将聊天的内容记录下来，并保存在文件当中。

难度：⭐⭐⭐⭐

支持的模式：仅支持在线模式

使用到的API及功能解读：

1.open(name, mode, encoding = 'utf-8)函数
open函数是Python内建库，可以在系统中打开或创建文件。
    name参数填入文件名称（包含后缀），字符型。
    mode参数，填入文件打开模式，包含只读 写入 和追加 等模式。字符型
        填入'r'表示文件打开模式为只读
        填入‘w’表示文件打开模式为写入模式，在这个模式下文件原有的数据会被清空，重新写入新的信息。
        填入'a'表示追加模式，表示会在原有数据的基础上，继续添加新的数据，默认会从文档最后面开始数据的添加。
    encoding = 'utf-8'
        在表示在utf-8的模式下进行文字解码，在utf-8模式下，写入中文不会乱码。

2.read(“string”) 函数
read是python的内建函数，在括号内填入要写入的内容

3.close()
文件在完成数据读写后，使用完成后，需要将文件进行关闭，实现文件的保存功能。如果没有close，则文件一致出于打开的状态，
会一直占用系统内存。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
import mkcloud

cyberpi.cloud.setkey("输入云服务授权码")
cyberpi.console.clear()
cyberpi.console.println("童芯派启动成功！")
cyberpi.wifi.connect("Maker-guest", "makeblock")
cyberpi.console.println("WIFI连接中...")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.led.on(0, 0, 255)
cyberpi.console.clear()
cyberpi.display.show_label("WiFi连接成功", 16, "center", index=0)
time.sleep(1)

chatfile = open("chatrecord.txt", 'a', encoding='utf-8')   # 打开文件为追加模式，解码为utf-8,并存放在chatfile变量下。
while True:
    if cyberpi.controller.is_press("a"):
        cyberpi.console.clear()
        cyberpi.console.println("开始语音识别")
        cyberpi.led.on(0, 255, 0)
        cyberpi.cloud.listen("chinese", 2)
        result = cyberpi.cloud.listen_result()
        chatfile.write("我说:" + result + "\n")      # 将语音识别的结果写入文件当中，并换行，
        cyberpi.console.println("识别结果： " + result)
        response = mkcloud.robot.chat(result)
        chatfile.write("机器人说:" + response + "\n")  # 将机器人反馈的结果写入文件当中，并换行。
        cyberpi.led.off()
        cyberpi.console.println(response)
        cyberpi.cloud.tts("zh", response)
    if cyberpi.controller.is_press("b"):
        chatfile.close()                             # 如果B键按下，关闭文件。
        cyberpi.console.clear()
        cyberpi.console.println("聊天结束")
        break
