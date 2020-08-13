""""
名称：001从灯光开始
硬件：童芯派
功能介绍：001程序，从点亮童芯派的灯光开始，点灯恒久远，LED永流传。

难度：⭐

支持的模式：上传 、在线

使用到的API及功能解读：
1.cyberpi.led.off()
  童芯派的.LED灯.熄灭

2.cyberpi.led.on(r, g, b,'all')
  童芯派的.LED灯.打开（颜色为（255，255，255），全部灯光）
         ’all‘ 表示所有灯光，此参数若不填写则默认点亮所有LED灯。
         将'all'可以替换为数字 1、2、3、4、5,对应相应位置的LED灯。
         r,g,b，三个参数的取值范围为0-255

"""

# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi                           # 导入童芯派第三方库，只有导入才能调用童芯派相应的功能。

cyberpi.led.off()                        # 灯光初始化，先熄灭所有的灯光
cyberpi.led.on(255, 255, 255, 'all')     # 打开童芯派的LED灯，设置灯光RGB值为255，255，255，即白灯。

# 拓展：
#     1.删除import cyberpi 后，程序能否正常运行？
#     2.尝试使用cyberpi.led.on() 设置不同的RGB值实现童芯派不同的灯光变幻。
