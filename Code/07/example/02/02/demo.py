import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('JD2019.xlsx')
#数据处理
df1=df[df['商品名称']=='零基础学Python（全彩版）'].sort_values('日期')
df1=df1[['北京','上海','广州','成都','武汉','沈阳','西安','日期']]
df1= df1.set_index('日期')          #将日期设置为索引
df1['全国销量']=df1.sum(axis=1)     #求和运算
#选取2019年数据
df1=df1['2019-01-01':'2019-12-01']
print(df1)
df1['January']=df1.iloc[0,7]
#定比分析（以2019年1月为基期，基点为1）
df1['base']=df1['全国销量']/df1['January']
x=[0,1,2,3,4,5,6,7,8,9,10,11]
y1=df1['全国销量']
y2=df1['base']
fig = plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']  #解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
ax1 = fig.add_subplot(111)                  #添加子图
plt.title('2019年全国销量定比分析')         #图表标题
#图表x轴标题
plt.xticks(x,['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'])
ax1.bar(x,y1,color = 'blue',label='left',alpha=0.5)
ax1.set_ylabel('全国销量（册）')            #y轴标签
ax2 = ax1.twinx()                           #添加一条y轴坐标轴
ax2.plot(x,y2,color='r',linestyle='-',marker='D',linewidth=2)
for a,b in zip(x,y2):
    plt.text(a, b+0.02, '%.3f' %b, ha='center', va= 'bottom',fontsize=9)
plt.show()