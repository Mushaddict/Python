from sklearn import linear_model
import numpy as np
x=np.array([[1,56],[2,104],[3,156],[4,200],[5,250],[6,300]])
y=np.array([7800,9000,9200,10000,11000,12000])
clf = linear_model.LinearRegression()
clf.fit (x,y)    #拟合线性模型
k=clf.coef_      #回归系数
b=clf.intercept_ #截距
x0=np.array([[7,170]])
#通过给定的x0预测y0，y0=截距+X值*回归系数
y0=clf.predict(x0) #预测值
print('回归系数：',k)
print('截距：',b)
print('预测值：',y0)
