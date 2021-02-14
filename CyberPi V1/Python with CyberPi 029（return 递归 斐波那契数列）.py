""""
名称：029 函数 递归 斐波那契数列
硬件： 童芯派
功能介绍：利用函数的递归在屏幕上显示斐波那契数列。

难度：⭐⭐⭐⭐⭐

支持的模式：上传、在线都支持

使用到的API及功能解读：
1.函数
  函数可以实现递归得功能,函数得递归可以看作函数反复调用自己的过程。
  举例：
  def plus(n)                   定义了一个求和函数，输入一个数值，可以得出从1到该数所有数值之和。
    if n == 1:                      如果数值为1：
        return 1                         则返回值为1
    else:                           否则：
        return n + plus(n-1)             返回当前的数值n + plus(n-1)  此时程序会再次调用函数plus()
                                         数值变为n-1,在plus(n-1)中，如果n-1不为1，则会再次调用函数plus()
                                         数值变为n-1-1，一次类推，直到n==1为止。
注意：随着递归的层级越来越多，运算速度会明显减慢。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi  # 导入童芯派的第三方库


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


cyberpi.console.clear()
scale = int(input("请输入一个正整数吗，用于生成斐波那契数列: "))
for i in range(1, scale+1):
    print(fib(i))
    cyberpi.console.println(fib(i))
cyberpi.console.println("生成完毕")
