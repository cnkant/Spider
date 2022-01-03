# encoding utf8
# 柱形图
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = Axes3D(fig)

# ax.plot_wireframe(X, Y, Z, cmap="hot")
ax.plot_surface(X, Y, Z, cmap="hot")
ax.contourf(X, Y, Z, offset=-1, cmap='hot')

ax.set_zlim(-1, 1)

plt.show()
