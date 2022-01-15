import numpy as np
from sklearn.cluster import KMeans
X=np.array([[1,10],[1,11],[1,12],[3,20],[3,23],[3,21],[3,25]])
kmodel = KMeans(n_clusters = 2)      #调用KMeans方法实现聚类（两类）
y_pred=kmodel.fit_predict(X)         #预测类别
print('预测类别：',y_pred)
print('分类簇的均值向量：','\n',kmodel.cluster_centers_)
print('类别标记：',kmodel.labels_)

