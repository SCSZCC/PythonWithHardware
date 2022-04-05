""""
名称：EXT 001 童芯派 Pygame 数据可视化显示
硬件： 童芯派 
功能介绍：
利用Pygame的绘图功能，实现对童芯派传感器读取到数值的显示


难度：⭐⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time
import pygame
import sys



def basic():
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (0, 350), (800,350),1)
    pygame.display.update()


pygame.init()
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("A new project")
basic()
x = 0
y = 0
y1 = cyberpi.get_bri() 
z = 0
z1 = cyberpi.get_loudness()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.aaline(screen, (0,255,0), (x, 300-2*y), (x+2,300-2*y1),1)
    pygame.draw.aaline(screen, (0,0,255), (x, 600-2*z), (x+2,600-2*z1),1)
    pygame.display.update()
    x += 2
    y = y1
    z = z1
    y1 = cyberpi.get_bri()
    z1 = cyberpi.get_loudness()
    if x > 800:
        basic()
        x = 0