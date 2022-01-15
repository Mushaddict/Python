import numpy as np                    #导入numpy模块
n1 = np.asarray([1,2,3])              #通过列表创建数组
n2 = np.asarray([(1,1),(1,2)])        #通过列表的元组创建数组
n3 = np.asarray((1,2,3))              #通过元组创建数组
n4= np.asarray(((1,1),(1,2),(1,3)))   #通过元组的元组创建数组
n5 = np.asarray(([1,1],[1,2]))        #通过元组的列表创建数组
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)