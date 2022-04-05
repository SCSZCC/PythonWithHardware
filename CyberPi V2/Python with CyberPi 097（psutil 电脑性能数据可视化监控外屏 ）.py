""""
名称：097 童芯派 pustil 电脑性能数据可视化监控外屏
硬件： 童芯派 
功能介绍：
利用Pustil模块获取电脑的内存和CPU使用状态，并通过童芯派的图表功能进行实时呈现。
成为电脑性能监控扩展屏幕。当超过

使用到的API及功能解读：

1.ram = psutil.virtual_memory()
获取电脑内存数据

2.rampercent = ram.percent 
获取电脑内存使用率

3.psutil.cpu_percent()
获取电脑CPU使用率

4.cyberpi.barchart.add(rampercent) 
绘制柱状图（注意：不同数据的需要通过设置画刷颜色的方式进行区隔
）

难度：⭐⭐⭐⭐
支持的模式：在线模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import psutil                                                          
import time
import cyberpi
cyberpi.chart.clear()                                                  
while True:                                                            
    ram = psutil.virtual_memory()
    rampercent = ram.percent   
    cpu = psutil.cpu_percent() 
    cyberpi.chart.set_name('RAM'+str(rampercent)+'% CPU'+str(cpu)+'%')   
    cyberpi.display.set_brush(0, 0, 255)
    cyberpi.barchart.add(rampercent)      
    cyberpi.display.set_brush(255, 0, 0) 
    cyberpi.barchart.add(cpu)     
    if cpu >= 80 or rampercent >= 95:  
        cyberpi.led.on(255,0,0) 
        cyberpi.audio.play('prompt-tone')   
    else:                                
        cyberpi.led.on(0,0,255)  
    time.sleep(0.2)               