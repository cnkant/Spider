import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
unemployment = pd.read_csv(r"pytest\数据可视化\hot-dog-places.csv")
num = len(unemployment) # 获取行数
# print(num)
ind = np.arange(num) # 横坐标
# print(ind)
fig, ax = plt.subplots()
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
mpl.rcParams["axes.unicode_minus"] = False
ax.set_title("1948-2010年间的美国失业率")
x = ind
y = unemployment["Value"]
plt.scatter(x, y)
plt.xlabel("8-李康")
plt.ylabel("失业率")
plt.savefig("pytest\\数据可视化\\8-李康.png")
plt.show()
