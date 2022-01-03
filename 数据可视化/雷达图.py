# 雷达图
import numpy as np
import matplotlib.pyplot as plt

y1 = np.random.rand(10) * 5 + 5
y2 = np.random.rand(10) * 5 + 5
y3 = np.random.rand(10) * 5 + 5
x = np.linspace(0, 2 * np.pi, 10)

fig = plt.figure(figsize=(4, 4))
ax = plt.subplot(111, projection='polar')

ax.plot(x, y1, '.--', label='y1')
ax.fill(x, y1, alpha=0.2)
ax.plot(x, y2, '.--', label='y2')
ax.fill(x, y2, alpha=0.2)
ax.plot(x, y3, '.--', label='y3')
ax.fill(x, y3, alpha=0.2)

plt.legend()
plt.show()
