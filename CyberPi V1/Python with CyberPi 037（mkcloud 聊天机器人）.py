"""
名称：037 mkcloud上的聊天机器人-小思
硬件： 童芯派
功能介绍：简单的模拟一个登录界面

难度：⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1. mkcloud.robot.chat(str)
str:字符串，填入要聊天的内容，返回值为字符串，为机器人给出的回复。


"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import mkcloud

while True:
    say = input("请输入要聊天内容:")
    response = mkcloud.robot.chat(say)
    print(response)
