""""
名称：095 童芯派 matplotlib 陀螺仪和散点图
硬件： 童芯派 
功能介绍：
结合童芯派与matplotlib的图表功能，获取陀螺仪的状态，并呈现在散点图上。
这个小点的位置会随陀螺仪状态的变化而变化。

使用到的API及功能解读：

1.plt.scatter(x, y)
根据数据绘制柱状图,x，y分别填入对应的数据。

2.plt.figure(figsize=(width, height))
用以设置图表的画布大小，width和hegiht表示长和宽。需要注意的是这里的单位是英寸。
这里的单位是英寸 是英寸。



难度：⭐⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi
import time
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.ion()
plt.figure(figsize=(15, 8))

while True:
    hum = cyberpi.humiture.get_humidity()
    temp = cyberpi.humiture.get_temp()
    plt.clf()
    y_locator = plt.MultipleLocator(10)
    x_locator = plt.MultipleLocator(10)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_locator)
    ax.xaxis.set_major_locator(x_locator)
    plt.ylim(-90,90)
    plt.xlim(-180,180)
    plt.scatter(x=0+cyberpi.get_roll(), y=0+cyberpi.get_pitch())
    plt.title('跟随陀螺仪变化位置的小点')
    plt.show()
    plt.pause(0.01)