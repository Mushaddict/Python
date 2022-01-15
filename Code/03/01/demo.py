import pandas as pd            #导入pandas模块
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 50)
df=pd.read_excel('data.xlsx')  #读取Excel文件
print(df.head())               #显示前5条数据

