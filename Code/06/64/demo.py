import numpy as np
price=np.array([34.5,36,37.8,39,39.8,33.6])  #创建“单价”数组
number=np.array([900,580,230,150,120,1800])  #创建“销售数量”数组
print('加权平均价：')
print(np.average(price,weights=number))
