import numpy as np
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('对数组元素求和：')
print(n.sum())
print('对数组元素按行求和：')
print(n.sum(axis=0))
print('对数组元素按列求和：')
print(n.sum(axis=1))