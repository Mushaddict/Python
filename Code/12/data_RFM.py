import pandas as pd
import numpy as np
data_all = pd.read_excel('./data/all.xlsx')   #读取Excel文件
#去除空值，订单付款时间非空值才保留
#去除买家实际支付金额为0的记录
data=data_all[data_all['订单付款时间'].notnull() & data_all['买家实际支付金额'] !=0]
data=data.copy()     #复制数据
#计算RFM值
data['最近消费时间间隔'] = (pd.to_datetime('2019-12-31') - pd.to_datetime(data['订单付款时间'])).values/np.timedelta64(1, 'D')
df=data[['订单付款时间','买家会员名','买家实际支付金额','最近消费时间间隔']]
df1=df.groupby('买家会员名').agg({'买家会员名':'size','最近消费时间间隔': 'min','买家实际支付金额':'sum'})
df2=df1.rename(columns={'买家会员名':'消费频率','买家实际支付金额':'消费金额'})
df2.to_excel('./data/RFM.xlsx') #导出结果