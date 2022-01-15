import numpy as np
x=np.array([4,7,3,2,8,5,1,9,6])
print('升序排序后的索引值：')
y = np.argsort(x)
print(y)
print('排序后的顺序重构原数组：')
print(x[y])
