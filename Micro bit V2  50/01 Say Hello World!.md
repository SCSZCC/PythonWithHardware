# 01 Say Hello World！
##### 程序简介：

在学习编程语言当中，常常学习到的第一个程序是在控制台上输出Hello World!。

Micro:bit是硬件，它没有控制台，但是它有点阵屏可以显示Hello World!



##### API：

###### 1.from moudle import * 

  from moudle import * 的方式可以将模块下的所有函数进行导入。

  

###### 2.display.scroll(str)

display.scroll函数可以在点阵屏上滚动显示文字，主要是英文。

str参数填入





##### 示例代码：

```python
from microbit import *     

display.scroll('Hello, World!')     

```

