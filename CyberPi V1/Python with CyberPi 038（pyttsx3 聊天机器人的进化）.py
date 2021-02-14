"""
名称：037 聊天机器人的进化
硬件： 童芯派
功能介绍：实现聊天机器人的TTS 播放

难度：⭐⭐⭐

支持的模式：仅支持在线模式

使用到的API及功能解读：
1. pyttsx3基本搭建框架，需要先安装依赖库pywin32模块

import pyttsx3                #导入pyttsx3模块
speak = pyttsx3.init()        #对pyttsx3模块进行初始化，初始化要放在程序前面。
speak.say('Hello World!') 	  #输入要转语音的文字
speak.runAndWait()            #播放合成的语音

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import mkcloud
import pyttsx3

speak = pyttsx3.init()
while True:
    say = input("请输入要聊天内容:")
    response = mkcloud.robot.chat(say)
    speak.say(response)
    print(response)
    speak.runAndWait()
