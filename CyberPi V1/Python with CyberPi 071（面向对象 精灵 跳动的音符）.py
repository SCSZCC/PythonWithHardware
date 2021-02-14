""""
名称：071 童芯派 精灵跳动的音符
硬件： 童芯派
功能介绍：
利用童芯派的精灵功能，设计music字母精灵，结合声音传感器实现音符跳动的功能。


难度：⭐⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time
import random
m = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000,
     0x4a90e2, 0x4a90e2, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x4a90e2,
     0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000,
     0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2,
     0x4a90e2, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2,
     0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2,
     0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000,
     0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000,
     0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000,
     0x000000, 0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x4a90e2, 0x4a90e2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000]
u = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000,
     0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623,
     0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623,
     0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623,
     0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000,
     0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000,
     0x000000, 0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623,
     0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000,
     0x000000, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623, 0xf5a623,
     0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000]
s = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b,
     0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b,
     0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000,
     0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xd0021b,
     0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b,
     0x000000, 0x000000, 0x000000, 0x000000, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b,
     0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xd0021b, 0xd0021b, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xd0021b, 0xd0021b, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b,
     0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000,
     0x000000, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b, 0xd0021b,
     0xd0021b, 0xd0021b, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000]
i = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf8e71c, 0xf8e71c, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0xf8e71c, 0xf8e71c, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0xf8e71c, 0xf8e71c, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf8e71c, 0xf8e71c,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0xf8e71c, 0xf8e71c, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf8e71c, 0xf8e71c, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0xf8e71c, 0xf8e71c, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf8e71c, 0xf8e71c, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0xf8e71c, 0xf8e71c, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf8e71c, 0xf8e71c, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000]
c = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2,
     0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2,
     0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000,
     0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x50e3c2,
     0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x50e3c2, 0x50e3c2,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x50e3c2, 0x50e3c2, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2,
     0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000,
     0x000000, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2, 0x50e3c2,
     0x50e3c2, 0x50e3c2, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
     0x000000, 0x000000, 0x000000]


class JumpNode:
    def __init__(self, x, pic, num):
        self.x = x
        self.num = num
        self.node = cyberpi.sprite()
        self.node.draw_pixels(pic)
        self.node.set_brush(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.node.set_align("bottom_mid")
        self.node.move_to(self.x, 128)
    def moving(self):
        loud = cyberpi.get_loudness("maximum")
        self.node.move_to(self.x, (128 - loud))
        cyberpi.led.on(0, 0, 0 + loud * 2.55, id=self.num)

        
m_1 = JumpNode(24, m, 1)
u_1 = JumpNode(44, u, 2)
s_1 = JumpNode(64, s, 3)
i_1 = JumpNode(84, i, 4)
c_1 = JumpNode(104, c, 5)
music_list = [m_1, u_1, s_1, i_1, c_1]
while True:
    for i in music_list:
        i.moving()
        cyberpi.screen.render()