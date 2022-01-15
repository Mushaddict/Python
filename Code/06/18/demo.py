import numpy as np
iterable = (x * 2 for x in range(5))   #遍历0~5并乘以2，返回可迭代对象
n = np.fromiter(iterable, dtype='int') #通过可迭代对象创建数组
print(n)

