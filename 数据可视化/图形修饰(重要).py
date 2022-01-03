# encoding = 'utf-8'
# 图形修饰

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2.3 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

p1 = plt.plot(x, y1)
p2 = plt.plot(x, y2)

plt.title("title")  # 标题
plt.xlabel("x label")  # 横轴名
plt.ylabel("y label")  # 纵轴名
plt.xticks(np.arange(0, 7), 'abcdefg')  # 设置轴刻度
# plt.legend()  # 图例
# 可以在每次plot时设置label，然后不传参使用
plt.legend((p1[0], p2[0]), ('y=sin(x)', 'y=cos(x)'), loc='upper left')
plt.box(True)  # 边框
plt.grid(True)  # 网格
plt.xlim(0, 2 * np.pi)  # x轴范围
plt.ylim(-1.5, 1.5)  # y轴范围

plt.show()
