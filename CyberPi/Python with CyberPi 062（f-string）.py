""""
名称：062 童芯派 f-string字符串格式化输出
硬件： 童芯派
功能介绍：
基于在线模式下的f-string格式化输出的使用。
难度：⭐⭐⭐
支持的模式：仅支持在线模式，MicroPython不支持f-string
使用到的API及功能解读：
f-string仅在python3.6及以上版本支持
f'内容{变量名} 内容{变量名} 内容{变量名}'
使用f前缀，在引号内使用大括号{}，在括号内填入格式化输出的变量。
详细请查阅pep498
"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi


while True:
    bri = cyberpi.get_bri()
    loud = cyberpi.get_loudness()
    cyberpi.display.label(f'光线:{bri} 声音{loud}', 16, 'center')