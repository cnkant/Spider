# encoding utf8
# 柱形图

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2, 11, 2)
y = 6 - np.arange(1, 6, 1)

N = 5
width = 0.35
ind = np.arange(N)
c = ['#ff0000', '#00ff00', '#ff0000', '#ff0000', '#ff0000']  # 设置每个柱的颜色
plt.bar(ind, x, width, color=c)
plt.bar(ind, y, width, bottom=x)  # 堆积柱形图
# barh是条形图

plt.show()
