""""
名称：091 童芯派 matplotlib 光线折线图
硬件： 童芯派 
功能介绍：
结合童芯派与matplotlib的图表功能，将童芯派上光线传感器获得的读值
通过matplotlib的图表进行呈现。


使用到的API及功能解读：
1.plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
调用系统字体支持中文，这里调用了微软雅黑。

2.plt.title('童芯派光线变化图')
设置图表名称

3.plt.ion()
打开交互绘图模式

4.plt.clf()
清空图表

5.plt.xlabel("次数")
设置x轴标签

6.plt.ylabel("光线强度")
设置Y轴标签

7.plt.plot(x, y)
根据数据绘制折线图,x，y分别填入对应的数据

8.plt.show()
显示图表

9.plt.pause(0.3)
设置图表刷新的间隔


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
data = []
x = []
count = 0

while True:
    bri = cyberpi.get_bri()
    data.append(bri)
    count += 1
    x.append(count)
    plt.clf()
    plt.xlabel("次数")
    plt.ylabel("光线强度")
    plt.plot(x, data)
    plt.title('童芯派光线变化图')
    plt.show()
    plt.pause(0.3)
    if cyberpi.controller.is_press('a'):
        data = []
        x = []