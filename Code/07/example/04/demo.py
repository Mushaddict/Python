import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel('成绩表.xlsx')
plt.rcParams['font.sans-serif']=['SimHei']                     #解决中文乱码
labels = np.array(['语文','数学','英语','物理','化学','生物']) #标签
dataLenth = 6  #数据长度
#计算女生、男生各科平均成绩
df1 = np.array(df[df['性别']=='女'].mean().round(2))
df2 = np.array(df[df['性别']=='男'].mean().round(2))
print(df1-df2)

#设置雷达图的角度，用于平分切开一个平面
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
df1 = np.concatenate((df1, [df1[0]]))    #使雷达图闭合
df2 = np.concatenate((df2, [df2[0]]))    #使雷达图闭合
angles = np.concatenate((angles, [angles[0]])) #使雷达图闭合
plt.polar(angles, df1, 'r--', linewidth=2,label='女生') #设置极坐标系,r--代表red和虚线
plt.fill(angles, df1,facecolor='r',alpha=0.5)         #填充
plt.polar(angles, df2,'b-', linewidth=2,label='男生') #设置极坐标系,bo代表blue和实心圆
plt.fill(angles, df2,facecolor='b',alpha=0.5)         #填充
plt.thetagrids(angles * 180/np.pi, labels)    #设置网格、标签
plt.ylim(0,140)                               #设置y轴上下限
plt.legend(loc='upper right',bbox_to_anchor=(1.2,1.1))  #图例及图例位置
plt.show()
