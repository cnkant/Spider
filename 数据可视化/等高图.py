# encoding utf8
# 等高线图
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contourf(X, Y, Z, 8, alpha=0.75, cmap=plt.cm.hot)  # 绘制颜色
C = plt.contour(X, Y, Z, 8, colors='black')  # 绘制等高线线
plt.clabel(C, inline=True, fontsize=10)  # 绘制等高线高度标识

plt.xticks(())
plt.yticks(())
plt.show()
