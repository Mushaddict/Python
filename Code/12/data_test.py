#对数据进行基本的探索
#返回缺失值个数以及最大最小值
import pandas as pd
data = pd.read_excel('./data/all.xlsx')                   #读取Excel文件
view = data.describe(percentiles = [], include = 'all').T #数据的基本描述
view['null'] = len(data)-view['count'] #describe()函数自动计算非空值数，需要手动计算空值数
view = view[['null', 'max', 'min']]
view.columns = [u'空值数', u'最大值', u'最小值'] #表头重命名
print(view)                         #输出结果
view.to_excel('./data/result.xlsx') #导出结果
