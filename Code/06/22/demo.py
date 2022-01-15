import numpy as np
a = np.arange(6)  #创建一个数组
n1 = np.full_like(a, 1)   #创建一个与数组a维度和数据类型相同的数组，以1填充
n2 = np.full_like(a,0.2)  #创建一个与数组a维度和数据类型相同的数组，以0.2填充
#创建一个与数组a维度和数据类型相同的数组，以0.2填充，浮点型
n3 = np.full_like(a, 0.2, dtype='float')
print(n1)
print(n2)
print(n3)