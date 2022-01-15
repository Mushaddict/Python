import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('TB.xls')
df1=df[['订单付款时间','买家实际支付金额']]
df1 = df1.set_index('订单付款时间')         #将“订单付款时间”设置为索引
plt.rcParams['font.sans-serif']=['SimHei']  #解决中文乱码
#按年统计数据
df_y=df1.resample('AS').sum().to_period('A')
print(df_y)
#按季度统计数据
df_q=df1.resample('Q').sum().to_period('Q')
print(df_q)
#绘制子图
fig = plt.figure(figsize=(8,3))
ax=fig.subplots(1,2)
df_y.plot(subplots=True,ax=ax[0])
df_q.plot(subplots=True,ax=ax[1])
#调整图表距上部和底部的空白
plt.subplots_adjust(top=0.95,bottom=0.2)
plt.show()