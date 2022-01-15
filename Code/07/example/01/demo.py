import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('car.xlsx')
df1=df.head(10)
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
x=df1['车型']
y=df1['1月销量']
#plt.grid(axis='y')
#调整图表距左的空白
plt.subplots_adjust(left=0.2)
#4个方向的坐标轴上的刻度线是否显示
plt.tick_params(bottom=False,left=False)
# 添加刻度标签
plt.yticks(range(10))
#图表标题
plt.title('2020年1月国产品牌汽车销量TOP10')
plt.barh(x, y,color='Turquoise')  #柱子蓝绿色
plt.show()