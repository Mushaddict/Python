import numpy as np
#创建二维数组
n1=np.array([[1,2],[3,4],[5,6]])
print(n1)
n2=np.delete(n1,2,axis=0)  #删除第3行
n3=np.delete(n1,0,axis=1)  #删除第1列
n4=np.delete(n1,(1,2),0)   #删除第2行和第3行
print('删除第3行后的数组：','\n',n2)
print('删除第1列后的数组：','\n',n3)
print('删除第2行和第3行后的数组：','\n',n4)