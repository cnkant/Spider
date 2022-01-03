# encoding utf8
# 饼图绘制
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其它']
sizes = [2, 5, 12, 70, 2, 9]
explode = (0, 0, 0, 0.1, 0, 0)

fig = plt.figure(figsize=(4, 4))
ax = plt.subplot(111)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
plt.title("饼图示例-8月份家庭支出")
plt.show()
