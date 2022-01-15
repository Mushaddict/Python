import numpy as np
import matplotlib.pyplot as plt
n1=plt.imread("flower.jpg")   #读取图片
plt.imshow(n1)   #传入数组显示对应颜色
#n1为三维的数组,最高维是图像的高，次高维是图像的宽，最低维[R,G,B]是颜色值
n2=np.array([0.299,0.587,0.114])   #灰度公式的固定值
x=np.dot(n1,n2) #将数组n1（RGB颜色值）和数组n2（灰度公式的固定值）中的每个元素进行点乘运算
plt.imshow(x,cmap="gray")   #传入数组显示灰度
plt.show()  #显示图像
