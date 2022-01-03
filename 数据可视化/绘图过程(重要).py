# encoding utf8
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 数据准备
x = np.arange(0.1, 2 * np.pi, 0.1)  # 线性空间，最小最大间隔
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x)
# y4 = np.arange(0, 10, 2)  # 产生从0到10间隔等差数列
# y5 = np.linspace(0, 2 * np.pi, 100)  # 产生从0到2pi间均匀100个点
# y6 = np.random.rand(10)  # 产生一个10元素向量，元素为0-1随机数

# 初始化
"""
可省略，这时使用默认参数
用 plt.figure() 中的两个参数控制图窗范围：
figsize   宽，高，单位英寸
dpi       指每英寸像素数
"""
fig = plt.figure(figsize=(6, 3), dpi=100)  # 改变图窗大小，单位英寸,dpi指每英寸像素数
ax = plt.subplot(111)

# 绘图
plt.subplot(121)  # 绘制子图
plt.plot(x, y1, "r-", label='y=sin(x)')  # 散点图
plt.plot(x, y2, "b-", label='y=cos(x)')  # 散点图
plt.subplot(122)
plt.plot(x, y3, "y-", label='y=log(x)')  # 散点图

# 图形修饰
plt.figure()

# 图形保存
"""
注意在show前保存，否则会存空白图
通过文件名即可指定保存格式
保存时可重新指定dpi
"""
# plt.savefig('save/img_svg.svg', dpi=100)
# plt.savefig('save/img_png.png')
# plt.savefig('save/img_pdf.pdf')

# 显示
plt.show()
