""""
名称：092 童芯派 matplotlib 温湿度折线图
硬件： 童芯派 mBuild温湿度传感器
功能介绍：
结合童芯派与matplotlib的图表功能，将温湿度传感器的读值在同一个折线图
图表当中进行呈现，并通过颜色进行区分。


使用到的API及功能解读：

1.plt.plot(x, y, color='r', label='湿度')
根据数据绘制折线图,x，y分别填入对应的数据。
color参数填入线段的颜色，通过颜色区分不同的数据组。
label用于设置折线图的标签名称，要在图表中显示图例需要
结合plt.legend()进行使用。

2.plt.legend()
显示图表中的图例


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
hum_data = []
temp_data = []
x = []
count = 0

while True:
    hum = cyberpi.humiture.get_humidity()
    temp = cyberpi.humiture.get_temp()
    hum_data.append(hum)
    temp_data.append(temp)
    count += 1
    x.append(count)
    plt.clf()
    plt.xlabel("次数")
    plt.ylabel("温湿度读值")
    plt.plot(x, hum_data, color = 'r', label='湿度')
    plt.plot(x, temp_data, color = 'b', label='温度')
    plt.title('童芯派温湿度传感器读值')
    plt.legend()
    plt.show()
    plt.pause(0.3)
    if cyberpi.controller.is_press('a'):
        temp_data = []
        hum_data = []
        count = []