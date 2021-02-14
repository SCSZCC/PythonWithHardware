""""
名称：096 童芯派 matplotlib 电量环形图
硬件： 童芯派 扩展板
功能介绍：
结合童芯派与matplotlib的图表功能，获取童芯派扩展板的电量，并通过环形图的进行显示。

使用到的API及功能解读：

1.plt.pie(data, labels = status, radius=1,wedgeprops = {'width': 0.3, 'edgecolor': 'w'})
根据数据绘制饼图（环形图），data填入列表数据，labels填入列表对应data的数据名称。
radius用以顶峰一绘制饼图的大小，wedgeprops数据类型为字典，设置环形图的宽度以及环形边缘的颜色。




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
    battery = cyberpi.get_battery()
    plt.clf()
    size = [battery, 100-battery]
    status = [f'剩余电量：{battery}%', f'已用电量：{100-battery}%']
    plt.pie(size, labels = status, radius=1,wedgeprops = {'width': 0.3, 'edgecolor': 'w'})
    plt.show()
    plt.title('童芯派扩展板电量环形图')
    plt.show()
    plt.pause(1)