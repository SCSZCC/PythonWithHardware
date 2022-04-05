""""
名称：033 Python中的字典 登录界面
硬件： 童芯派
功能介绍：简单的模拟一个登录界面，通过字典对用户名和密码进行判定

难度：⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.字典  字典是Python当中的一种数据类型。字典和其它数据类型相似，也需要创建变量进行存储。
       字典是另一种可变的容器模型。
       dict = {key1: value1, key2: value2}
       key1表示键，可以自定义键名，value1表示键值。
       通过dict[key1]的方式就可以获得key1对应的键值value1。



"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time

userdict = {'alice': 12345, 'john': 23333}     # 创建字典userdict,键设为用户名，键值设为密码

while True:                                    # 重复执行：
    cyberpi.console.clear()                        # 清空屏幕
    cyberpi.console.print("User: ")                # 显示user:
    username = input("User: ")                     # 提示输入用户名 ，并存放在变量username当中
    cyberpi.console.println(username)              # 在屏幕上显示输入的用户名
    cyberpi.console.print("password: ")            # 显示password:
    password = int(input("password: "))            # 提示输入密码，并存放在变量password当中
    cyberpi.console.print("******")                # 在屏幕上显示*****
    if username not in userdict:                   # 判定输入的用户名是否在字典的键当中：
        cyberpi.console.clear()                    #     如果不存在，清空屏幕
        cyberpi.display.show_label("用户不存在", 24, "center", index=0)    # 屏幕显示用户不存在
        time.sleep(1)                                      # 等待一秒
    else:                                          # 否则：
        if password == userdict[username]:              # 判定密码的值是否是用户名在字典中对应键所对应的键值
            cyberpi.console.clear()                     # 清空屏幕
            cyberpi.display.show_label("Welcome", 24, "center", index=0)  # 屏幕显示welcome
            break                                           # 停止循环
        else:                                           # 否则
            cyberpi.console.clear()                     # 清空屏幕
            cyberpi.display.show_label("密码错误", 24, "center", index=0)  # 屏幕显示密码错误
            time.sleep(1)                                   # 等待1秒
