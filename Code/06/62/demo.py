import numpy as np
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('对数组元素求平均值：')
print(n.mean())
print('对数组元素按行求平均值：')
print(n.mean(axis=0))
print('对数组元素按列求平均值：')
print(n.mean(axis=1))