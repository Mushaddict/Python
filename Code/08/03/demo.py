from sklearn.svm import LinearSVR              # 导入线性回归类
from sklearn.datasets import load_boston      # 导入加载波士顿数据集
from pandas import DataFrame                     # 导入DataFrame
boston = load_boston()                            # 创建加载波士顿数据对象
# 将波士顿房价数据创建为DataFrame对象
df = DataFrame(boston.data, columns=boston.feature_names)
df.insert(0,'target',boston.target)             # 将价格添加至DataFrame对象中
data_mean = df.mean()                              # 获取平均值
data_std = df.std()                                 # 获取标准偏差
data_train = (df - data_mean) / data_std       # 数据标准化
x_train = data_train[boston.feature_names].values       # 特征数据
y_train = data_train['target'].values                      # 目标数据
linearsvr = LinearSVR(C=0.1)                                  # 创建LinearSVR()对象
linearsvr.fit(x_train, y_train)                              # 训练模型
# 预测，并还原结果
x = ((df[boston.feature_names] - data_mean[boston.feature_names]) / data_std[boston.feature_names]).values
# 添加预测房价的信息列
df[u'y_pred'] = linearsvr.predict(x) * data_std['target'] + data_mean['target']
print(df[['target', 'y_pred']].head())                            #输出真实价格与预测价格
