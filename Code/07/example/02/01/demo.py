import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_excel('JD2019.xlsx')
#数据处理，提取2019年2月和2020年2月的数据
df= df.set_index('日期') # 将日期设置为索引
df1=pd.concat([df['2019-02'],df['2020-02']])
df1=df1[df1['商品名称']=='零基础学Python（全彩版）']
df1=df1[['北京','上海','广州','成都','武汉','沈阳','西安']]
df2=df1.T   #行列转置
x=np.array([0,1,2,3,4,5,6])
y1=df2['2019-02-01']
y2=df2['2020-02-01']
#同比增长率
df2['rate']=((df2['2020-02-01']-df2['2019-02-01'])/df2['2019-02-01'])*100
y=df2['rate']
print(y)
width =0.25                                     #柱子宽度
plt.rcParams['font.sans-serif']=['SimHei']      #解决中文乱码
plt.title('全国各地区销量及同比增长情况')       #图表标题
plt.ylabel('销售数量（册）')                    #y轴标签
#x轴标签
plt.xticks(x,['北京','上海','广州','成都','武汉','沈阳','西安'])
#双柱形图
plt.bar(x,y1,width=width,color = 'orange',label='2019年2月')
plt.bar(x+width,y2,width=width,color = 'deepskyblue',label='2020年2月')
# 增长率标签
for a, b in zip(x,y):
    plt.text(a,b,('%.1f%%' % b), ha='center', va='bottom', fontsize=11)
plt.legend()
plt.show()