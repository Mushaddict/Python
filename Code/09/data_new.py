import pymysql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()   #解决图表显示日期出现警告信息
#连接MySQL数据库，指定密码（passwd）和数据库（db）
conn = pymysql.connect(host = "localhost",user = 'root',passwd ='root',db = 'test',charset="utf8")
sql_query = 'SELECT * FROM test.user'     #SQL查询语句
data = pd.read_sql(sql_query, con=conn)   #读取MySQL数据
conn.close()         # 关闭数据库连接
data=data[['username','addtime']]         #提取指定列数据
data.rename(columns = {'addtime':'注册日期','username':'用户数量'},inplace=True)  #列重命名
data['注册日期'] = pd.to_datetime(data['注册日期']) #将数据类型转换为日期类型
data = data.set_index('注册日期')     #将日期设置为索引
data=data['2018-04-01':'2018-04-30']  #提取指定日期数据
#按天统计新注册用户
df=data.resample('D').size().to_period('D')
df.to_excel('result1.xlsx',index=False)# 导出数据为Excel文件
x=pd.date_range(start='20180401', periods=30)
y=df
#绘制折线图
sns.set_style('darkgrid')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.title('新用户注册时间分布图')              #图表标题
plt.xticks(fontproperties = 'Times New Roman', size = 8,rotation=20)#X轴字体大小
plt.plot(x,y)
plt.xlabel('注册日期')
plt.ylabel('用户数量')
plt.show()