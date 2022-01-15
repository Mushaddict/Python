import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                    '学生姓名':['明日同学','高猿员','钱多多']})
print(df1)
df2 = pd.DataFrame({'编号':['mr001','mr001','mr003'],
                    '语文':[110,105,109],
                    '数学':[105,88,120],
                    '英语':[99,115,130],
                    '时间':['1月','2月','1月']})
print(df2)
df_merge=pd.merge(df1,df2,on='编号')
print(df_merge)

