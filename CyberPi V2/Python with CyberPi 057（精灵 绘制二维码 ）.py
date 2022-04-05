""""
名称：057 童芯派 精灵 生成一个二维码
硬件： 童芯派
功能介绍：
利用童芯派的精灵功能，在屏幕上生成一个二维码
难度：⭐⭐⭐
支持的模式：仅支持上传模式，请使用慧编程Python进行程序编写和程序烧录。
使用到的API及功能解读：
1.通过变量（即对象名称）创建精灵对象。 对象名 = cyberpi.sprite()
    对象名称= cyberpi.sprite()
    示例：qrcode = cyberpi.sprite()
2.通过对象调用精灵对象的方法。  对象名.draw_qrcode()
  示例：qrcode.draw_qrcode(str) # 该API根据输入的信息绘制二维码,信息内容为字符串。
3.调整精灵对象大小  对象名.set_size()
  示例：qrcode.set_size(size = int)  # 调整精灵对象的尺寸
4.显示的精灵  对象名.show()
  示例：qrcode.show()
5.屏幕渲染
  用以在屏幕上生成图像，绘制的精灵如果要显示则必须调用此API
  cyberpi.screen.render()
"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi

qrcode = cyberpi.sprite()
qrcode.draw_qrcode("Welcome")
qrcode.set_size(size=300)
qrcode.show()
cyberpi.screen.render()