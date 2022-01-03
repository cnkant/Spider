# encoding utf8
# 折线图图和子图绘制

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0.1, 2*np.pi, 0.1)  # 线性空间，最小最大间隔
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x)

plt.subplot(121)
plt.plot(x, y1, "r-")  # 散点图
plt.plot(x, y2, "b-")  # 散点图
plt.subplot(122)  # 绘制子图
plt.plot(x, y3, "y-")  # 散点图


plt.show()
