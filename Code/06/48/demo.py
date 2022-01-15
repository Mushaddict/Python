import numpy as np
#创建数组
n1 = np.array([1, 2, 3])
n2= np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print('数组相乘结果为：','\n', n1*n2) #数组相乘
print('数组点乘结果为：','\n', np.dot(n1, n2)) #数组点乘
print(np.multiply(n1,n2))