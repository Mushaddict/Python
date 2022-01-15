import numpy as np          #导入numpy模块
n1 = np.array([1,2,3])      #创建数组
n2 = np.array(n1,copy=True) #复制数组
n2[0]=3                     #修改第1行数组为3
n2[2]=1                     #修改第2行数组为1
print(n1)
print(n2)
