import numpy as np
# 创建一个3*3的零矩阵
data1 = np.mat(np.zeros((3,3)))
print('3*3的零矩阵：')
print(data1)
# 创建一个2*4的1矩阵
data1 = np.mat(np.ones((2,4)))
print('2*4的1矩阵：')
print(data1)

#使用rand()函数创建一个3*3在0~1之间随机产生的二维数组
data1 = np.mat(np.random.rand(3,3))
print('3*3在0~1之间随机产生的二维数组：')
print(data1)

#创建一个1~8之间的随机整数矩阵
data1 = np.mat(np.random.randint(1,8,size=(3,5)))
print('1~8之间的随机整数矩阵：')
print(data1)

#创建对角矩阵
print('对角矩阵：')
data1 = np.mat(np.eye(2,2,dtype=int)) #2*2对角矩阵
print(data1)
data1 = np.mat(np.eye(4,4,dtype=int)) #4*4对角矩阵
print(data1)

#创建对角线矩阵
print('对角线矩阵：')
a = [1,2,3]
data1 = np.mat(np.diag(a))  #对角线1、2、3矩阵
print(data1)
b = [4,5,6]
data1 = np.mat(np.diag(b))  #对角线4、5、6矩阵
print(data1)
