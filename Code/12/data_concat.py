import pandas as pd
#读取Excel文件
df_2018=pd.read_excel('./data/2018.xlsx')
df_2019=pd.read_excel('./data/2019.xlsx')
#抽取指定列数据
df_2018=df_2018[['买家会员名','买家实际支付金额','订单付款时间']]
df_2019=df_2019[['买家会员名','买家实际支付金额','订单付款时间']]
#数据合并与导出
dfs=pd.concat([df_2018,df_2019])
print(dfs.head())    #输出部分数据
dfs.to_excel('./data/all.xlsx',index=False)
