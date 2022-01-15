import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
sns.set_style('darkgrid')
n = np.random.normal(0, 0.1, 1000)   #生成均值为0，标准差为0.1的一维正态分布样本1000个
print(n)
sns.distplot(n)                      #直方图
plt.show()# 显示