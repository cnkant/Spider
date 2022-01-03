# encoding = 'utf-8'
# 柱形图
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = pd.read_csv("支持率民意调查.csv")
name = data['问题']
agree = data['支持']
disagree = data['反对']

width = 0.35
ind = np.arange(13)
# plt.barh(ind, agree, color='b')
# plt.barh(ind, disagree, left=agree, color='r')
# 把pandas数据传入data，就可以直接使用下标名做参数
plt.barh(ind, '支持', data=data, color='g')
plt.barh(ind, '反对', data=data, left='支持', color='r')
plt.yticks(ind, name)
plt.show()
