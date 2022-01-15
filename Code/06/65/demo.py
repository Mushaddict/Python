import numpy as np
n=np.array([34.5,36,37.8,39,39.8,33.6])  #创建“单价”数组
# 数组排序后，查找中位数
sort_n = np.msort(n)
print('数组排序：')
print(sort_n)
print('数组中位数为：')
print(np.median(sort_n))

