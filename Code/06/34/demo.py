import numpy as np
n=np.arange(6)      #创建一维数组
print(n)
n1=n.reshape(2,3)   #将数组重塑为2行3列的二维数组
print(n1)

n=np.array(['床','前','明','月','光','疑','是','地','上','霜','举','头','望','明','月','低','头','思','故','乡'])
n1=n.reshape(4,5)
print(n1)