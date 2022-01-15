import pymysql
import pandas as pd
import matplotlib.pyplot as plt
#连接MySQL数据库，指定密码（passwd）和数据库（db）
conn = pymysql.connect(host = "localhost",user = 'root',passwd ='root',db = 'test',charset="utf8")
sql_query = 'SELECT * FROM test.user'     #SQL查询语句
data = pd.read_sql(sql_query, con=conn)   #读取MySQL数据
conn.close()         # 关闭数据库连接
data=data[['username','addtime']]         #提取指定列数据
data.rename(columns = {'addtime':'注册日期','username':'用户数量'},inplace=True)  #列重命名
data['注册日期'] = pd.to_datetime(data['注册日期']) #将数据类型转换为日期类型
data = data.set_index('注册日期') # 将日期设置为索引
#按月统计每一年的注册用户
index=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
df_2017=data['2017']
df_2017=df_2017.resample('M').size().to_period('M')
df_2017.index=index
df_2018=data['2018']
df_2018=df_2018.resample('M').size().to_period('M')
df_2018.index=index
df_2019=data['2019']
df_2019=df_2019.resample('M').size().to_period('M')
df_2019.index=index
dfs=pd.concat([df_2017,df_2018,df_2019],axis=1)
#设置列索引
dfs.columns=['2017年','2018年','2019年']
dfs.to_excel('result2.xlsx',index=False)# 导出数据为Excel文件
#绘制折线图
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.title('年度注册用户分析图')
x=index
y1=dfs['2017年']
y2=dfs['2018年']
y3=dfs['2019年']
plt.plot(x,y1,label='2017年',color='b',marker='o')
plt.plot(x,y2,label='2018年',color='g',marker='o')
plt.plot(x,y3,label='2019年',color='r',marker='o')
#添加文本标签
for a,b1,b2,b3 in zip(x,y1,y2,y3):
    plt.text(a,b1+200,b1,ha = 'center',va = 'bottom',fontsize=8)
    plt.text(a,b2+100,b2,ha='center', va='bottom', fontsize=8)
    plt.text(a,b3+200,b3,ha='center', va='bottom', fontsize=8)
x = range(0, 12, 1)
plt.xlabel('注册日期')
plt.ylabel('用户数量')
plt.legend()
plt.show()
