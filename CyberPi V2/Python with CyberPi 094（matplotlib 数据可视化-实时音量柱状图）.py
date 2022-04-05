""""
名称：094 童芯派 matplotlib 音量柱状图-f-string
硬件： 童芯派 mBuild温湿度传感器
功能介绍：
结合童芯派与matplotlib的图表功能，将声音传感器的读值通过柱状图的方式
进行实时呈现。
应用f-string字符串格式化输出的方式在图例上显示实时数值。

使用到的API及功能解读：

1.plt.bar(x, y, align='center',label='数据名称')
根据数据绘制柱状图,x，y分别填入对应的数据。
align设置柱形图的对其方式，'center'表示中间对齐
label用于设置折线图的标签名称，要在图表中显示图例需要
结合plt.legend()进行使用。




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
    loud = cyberpi.get_loudness()
    plt.clf()
    plt.xlabel("数据名称")
    plt.ylabel("音量读值")
    y_locator = plt.MultipleLocator(5)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_locator)
    plt.ylim(0,100)
    plt.bar('音量', loud, align='center',label=f'温度{loud}')
    plt.title('童芯派声音传感器读值')
    plt.legend()
    plt.show()
    plt.pause(0.01)