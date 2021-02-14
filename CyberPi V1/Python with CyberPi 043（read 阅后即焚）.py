""""
名称：043 阅后即焚
硬件： 童芯派
功能介绍：读取文件的信息后，就会自动将读取到的信息进行删除。

难度：⭐⭐⭐⭐

支持的模式：仅支持在线模式

使用到的API及功能解读：

1.read()函数
python的内建函数，通过read函数可以读取到文件中的数据



"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time


cyberpi.led.off()
cyberpi.console.clear()
while True:
    if cyberpi.controller.is_press("a"):
        chatfile = open("chatrecord.txt", 'r', encoding='utf-8')  # 打开文件为追加模式，解码为utf-8,并存放在chatfile变量下。
        message = chatfile.read()                                 # 用变量存放 读取（read）所打开文件中的数据
        for i in message:                                         # 将读取的数据逐字在屏幕上进行打印。
            cyberpi.console.print(i)
            time.sleep(0.01)
        cyberpi.console.println("消息即将抹除")
        chatfile.close()
        chatfile = open("chatrecord.txt", 'w', encoding='utf-8')  # 打开文件为写入模式，解码为utf-8,并存放在chatfile变量下。
        chatfile.write("404 Not Found")                           # 写入模式会先将文件内的数据进行清空，再写入。
        cyberpi.console.clear()
        chatfile.close()

