import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
#引入sklearn模块，导入KMeans方法（K均值聚类算法）
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#读取数据并进行聚类分析
data = pd.read_excel('./data/transformdata.xlsx') #读取数据
cdata = pd.read_excel('./data/RFM.xlsx') #读取数据
cdata=cdata[['买家会员名','最近消费时间间隔','消费频率','消费金额']]    #提取指定列数据
k = 4                            #设置聚类类别数
kmodel = KMeans(n_clusters = k)  #创建聚类模型
kmodel.fit(data) #训练模型
#标记原始数据的类别
cdata= pd.concat([cdata, pd.Series(kmodel.labels_, index=cdata.index)], axis=1)
#重命名最后一列为“类别”
cdata.columns=['买家会员名','R-最近消费时间间隔','F-消费频率','M-消费金额','类别']
cdata.to_excel('./data/client.xlsx')
# 按照类别分组统计R, F, M的指标均值
data_mean = cdata.groupby(['类别']).mean()
print(data_mean)
data_mean.to_excel('./data/client_mean.xlsx')
new=data_mean.mean()
#增加一行RFM平均值（忽略索引）,判断RFM值的高低
df=data_mean.append(new,ignore_index=True)
print(df)

r1=pd.Series(kmodel.labels_).value_counts()
r2=pd.DataFrame(kmodel.cluster_centers_)
r=pd.concat([r2,r1],axis=1)
r.columns=list(data.columns)+[u'聚类数量']
r3 = pd.Series(kmodel.labels_,index=data.index)  #类别标记
r = pd.concat([data,r3], axis=1)                 #数据合并
r.columns = list(data.columns)+[u'聚类类别']
r.to_excel('./data/type.xlsx')                   #导出数据
plt.rcParams['font.sans-serif']=['SimHei']       #解决中文乱码
plt.rcParams['axes.unicode_minus']=False         #解决负号不显示
#密度图
for i in range(k):
  cls=data[r[u'聚类类别']==i]
  cls.plot(kind='kde',linewidth=2,subplots=True,sharex=False)
  plt.suptitle('客户群=%d;聚类数量=%d' %(i,r1[i]))
plt.show()