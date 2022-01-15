import numpy as np
#np.set_printoptions(threshold=np.inf)
#输出时打印不换行
np.set_printoptions(linewidth=800)
#n = np.logspace(0,63,64,base=2,dtype='int')
n = np.logspace(0,63,64,base=2,dtype='uint64')

#数组重塑8*8矩阵
print(n.reshape(8,8))
