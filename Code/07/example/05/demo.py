import pandas as pd
import matplotlib.pyplot as plt
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
df_y = pd.read_excel('展现量.xlsx')
df_x = pd.read_excel('费用.xlsx')
df_x= df_x.set_index('日期')                #将日期设置为索引
df_y= df_y.set_index('日期')                #将日期设置为索引
df_x.index = pd.to_datetime(df_x.index)     #将数据的索引转换为datetime类型
df_x=df_x.resample('D').sum()               #按天统计费用
data=pd.merge(df_x,df_y,on='日期')          #数据合并

plt.rcParams['font.sans-serif']=['SimHei']  #解决中文乱码
plt.xlabel('费用成本（x）')
plt.ylabel('广告展现量（y）')
plt.scatter(data['费用'], data['展现量'])   #绘制散点图，以“费用”和“展现量”作为横纵坐标
plt.show()

#相关系数
print(data.corr())
