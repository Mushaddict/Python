import numpy as np
n = np.array([1.55, 6.823,100,0.1189,3.1415926,-2.345])  #创建数组
print(np.around(n))  #四舍五入取整
print(np.around(n, decimals=2)) #四舍五入保留小数点两位
print(np.around(n, decimals=-1))#四舍五入取整到小数点左侧