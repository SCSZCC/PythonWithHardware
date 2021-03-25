""""
名称：EXT 001 童芯派 Matplotlib subplot多图表生成
硬件： 童芯派 
功能介绍：
利用subplot功能，在一个画板当中生成多个图表。


难度：⭐⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
from matplotlib import pyplot as plt
import time
import cyberpi

loud_list = []
bri_list = []
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   # 加载中文字体，这里加载的是电脑的自带的微软雅黑字体
plt.ion()
plt.figure(figsize=(10,10))
plt.figure(1)
x_locator = plt.MultipleLocator(5)
y_locator = plt.MultipleLocator(5)
while True:
    loud = cyberpi.get_loudness()
    bri = cyberpi.get_bri()
    loud_list.append(loud)
    bri_list.append(bri)
    battery = cyberpi.get_battery()
    size = [battery, 100-battery]
    status = [f'剩余电量：{battery}%', f'已用电量：{100-battery}%']
    ax1 = plt.subplot(221)
    plt.title('光线折线图')
    ax1.plot(bri_list)
    ax2 = plt.subplot(222)
    plt.title('声音柱状图')
    ax2.xaxis.set_major_locator(x_locator)
    ax2.yaxis.set_major_locator(y_locator)
    plt.ylim(0,100)
    ax2.bar('sound', loud)
    ax3 = plt.subplot(223)
    ax3.xaxis.set_major_locator(x_locator)
    ax3.yaxis.set_major_locator(y_locator)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.title('声音、音量散点图')
    ax3.scatter(loud_list,bri_list)
    ax4 = plt.subplot(224)
    ax4.pie(size, labels = status, radius=1,wedgeprops = {'width': 0.3, 'edgecolor': 'w'})
    plt.title('童芯派电量')
    plt.pause(0.2)
    plt.clf()
    if cyberpi.controller.is_press('a'):
        break
    if len(bri_list) > 500:
        bri_list = []
        loud_list = []