import numpy as np
n1 = np.arange(10)  #创建一个一维数组
print(n1)
print(np.where(n1>5,2,0))  #大于5输出1,不大于5输出0
n2=n1[np.where(n1>5)]
print(n2)