# encoding utf8
# 柱形图
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)
size = 1000*((x - 0.5) * (x - 0.5) + (y - 0.5) * (y - 0.5))

plt.scatter(x, y, s=size)
# s控制大小，c控制颜色
plt.show()
