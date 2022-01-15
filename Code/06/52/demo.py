import numpy as np
n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])  #创建数组
n2 = np.array([10, 10, 10])
print('两个数组相加：')
print(np.add(n1, n2))
print('两个数组相减：')
print(np.subtract(n1, n2))
print('两个数组相乘：')
print(np.multiply(n1, n2))
print('两个数组相除：')
print(np.divide(n1, n2))