import numpy as np
#创建二维数组
n1=np.array([[1,2],[3,4],[5,6]])
n2=np.array([[10,20],[30,40],[50,60]])
print(np.hstack((n1,n2)))     #水平方向增加数据
print(np.vstack((n1,n2)))     #垂直方向增加数据


