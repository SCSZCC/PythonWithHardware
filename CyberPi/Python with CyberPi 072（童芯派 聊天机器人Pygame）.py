""""
名称：072 童芯派 有聊天窗口的聊天机器人
硬件： 童芯派
功能介绍：
利用硬件上内置的语音识别服务，结合mkcloud聊天机器人库与Pygame设计
一个具备可视化界面的聊天机器人
# 需要配合字体文件与背景文件的使用


难度：⭐⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import mkcloud
import pygame
import time
import sys


class WordText:
    """用于在Pygame中进行文字生成"""
    def __init__(self, font='', size=0, color=(0, 0, 0)):
        self._font = font
        self._size = size
        self._color = color
        self._setting = pygame.font.Font(self._font, self._size)

    def setWord(self, word=''):
        self._word = word
        self._render = self._setting.render(self._word, True, self._color)
        self._rect = self._render.get_rect()

    def setLoaction(self, centery=0):
        self._centery = centery
        self._rect.midleft = (30, self._centery)

    def getLoaction(self):
        if self._rect.right >= 380:
            return False

    def wordShow(self):
        screen.blit(self._render, self._rect.midleft)
        pygame.display.update()

class ChatSend(WordText):
    def setLoaction(self, centery = 0):
        self._centery = centery
        self._centerx = 419 - (self._rect.right - self._rect.left + 30)
        self._rect.midleft = (self._centerx, self._centery)


def clearsrceen(y):
    if y > 580:
        time.sleep(1)
        y = 50
        screen.blit(bg, bgrect)
        pygame.display.update()
    else:
        y += 40
    return y


pygame.init()
screensize = (419, 720)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("chat chat chat it up robot")
bg = pygame.image.load(".\image\\bg2.png")
bgrect = bg.get_rect()
screen.blit(bg, bgrect)
pygame.display.update()


cyberpi.cloud.setkey("从慧编程中获取云服务授权码")  #输入自己的云服务授权码
cyberpi.console.clear()
cyberpi.console.println("童芯派启动成功！")
cyberpi.wifi.connect("WiFi名称", "WiFi密码")
cyberpi.console.println("WIFI连接中...")
while not cyberpi.wifi.is_connect():
    pass
cyberpi.led.on(0, 0, 255)
cyberpi.console.println("童芯派连接成功")
time.sleep(1)
cyberpi.console.println("按下A键准备开始聊天")
sayprint = ChatSend("normal2.ttf", 20)
responseprint = WordText("normal2.ttf", 20, (255, 0, 255))
begin = 10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if cyberpi.controller.is_press("A"):
        begin = clearsrceen(begin)
        cyberpi.led.on(0, 255, 0)
        cyberpi.cloud.listen("chinese", 2)
        say = cyberpi.cloud.listen_result()
        cyberpi.led.off()
        sayprint.setWord(say)
        sayprint.setLoaction(begin)
        sayprint.wordShow()
        begin = clearsrceen(begin)
        response = mkcloud.robot.chat(say)
        new_a = 0
        for i in range(len(response) + 1):
            a = response[new_a:i]
            responseprint.setWord(a)
            responseprint.setLoaction(begin)
            if responseprint.getLoaction() == False:
                begin += 20
                new_a = i
                a = response[new_a:i]
            else:
                responseprint.wordShow()
                time.sleep(0.05)
            if begin > 580:
                begin = clearsrceen(begin)

