import numpy as np
n=np.array([[4,7,3],[2,8,5],[9,1,6]])
print('数组排序：')
print(np.sort(n))
print('按行排序：')
print(np.sort(n,axis=0))
print('按列排序：')
print(np.sort(n,axis=1))
