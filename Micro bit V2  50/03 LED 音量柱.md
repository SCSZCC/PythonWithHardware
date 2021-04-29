# 03 LED 音量柱
##### 程序简介：

在Micro:bit V2的版本上增加了一个音量传感器。可以检测外部环境的音量大小。利用检测到音量大小控制LED点阵屏的变化。从而实现音量柱的效果。



##### API：

###### 1.Image("")

用以自定义LED点阵屏的图案。需要对所有的LED状态进行定义。

Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "99999")   括号中的数字表示亮度，最小为0，最大为9。每一行对应LED点阵屏上的位置



###### 2.microphone.sound_level()

返回麦克风监测到的环境音量。返回数值区间为0-255。



##### 编程知识：

多条件分支结构

比较运算



##### 示例代码：

```python
from microbit import *


level_1 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "99999")
level_2 = Image("00000:"
              "00000:"
              "00000:"
              "99999:"
              "99999")
level_3 = Image("00000:"
              "00000:"
              "99999:"
              "99999:"
              "99999")
level_4 = Image("00000:"
              "99999:"
              "99999:"
              "99999:"
              "99999")
level_5 = Image("99999:"
              "99999:"
              "99999:"
              "99999:"
              "99999")
              
while True:
    loud = microphone.sound_level()
    if loud < 20:
        display.clear()
    elif 20<loud<95:
        display.show(level_1)
    elif 95<loud<135:
        display.show(level_2)
    elif 135<loud<175:
        display.show(level_3)
    elif 175<loud<215:
        display.show(level_4)
    elif 215<loud<255:
        display.show(level_5)
```

