""""
名称：093 童芯派 matplotlib 温湿度柱状图
硬件： 童芯派 mBuild温湿度传感器
功能介绍：
结合童芯派与matplotlib的图表功能，将温湿度传感器的读值通过柱状图的方式
进行实时呈现。

使用到的API及功能解读：

1.plt.bar(x, y, align='center',label='数据名称')
根据数据绘制柱状图,x，y分别填入对应的数据。
align设置柱形图的对其方式，'center'表示中间对齐
label用于设置折线图的标签名称，要在图表中显示图例需要
结合plt.legend()进行使用。

2.y_loactor = plt.MultipleLocator(5)
用以设置y轴的刻度间隔单位，并存放在变量里，这里设置了5，即每五个单位一个刻度。

3.ax = plt.gca()
表示用ax变量获得当前的子图。或者简单粗暴的理解为获得当前绘制图表的坐标轴。

4.ax.yaxis.set_major_locator(y_locator)
设置y轴的刻度为y_loactor设置的倍数

5.plt.ylim(0,100)
设置图表y轴的数值区间为0-100。



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

while True:
    hum = cyberpi.humiture.get_humidity()
    temp = cyberpi.humiture.get_temp()
    plt.clf()
    plt.xlabel("数据名称")
    plt.ylabel("温湿度读值")
    y_locator = plt.MultipleLocator(5)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_locator)
    plt.ylim(0,100)
    plt.bar('温度', temp, align='center',label='温度')
    plt.bar('湿度', hum, align='center',label='湿度')
    plt.title('童芯派温湿度传感器读值')
    plt.legend()
    plt.show()
    plt.pause(0.3)