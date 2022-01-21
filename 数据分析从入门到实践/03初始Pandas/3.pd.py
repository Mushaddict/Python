#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.set_option('display.unicode.east_asian_width', True)
data = [[2, 3, 4], [12, 34, 56], [32, 45, 23]]
index = [0, 1, 2]
columns = ['语文', '英语', '数学']


# In[5]:


df = pd.DataFrame(data = data, index = index, columns = columns)
df


# In[7]:


for col in df.columns : 
    series = df[col]
    print(series)


# In[9]:


df = pd.DataFrame(data = data, columns = columns)
df


# In[11]:


df = pd.DataFrame({
    '语文': [110, 105, 99], 
    '数学': [105, 88, 75], 
    '英语': [109, 120, 130], 
    '班级': '高一7班'
})
df


# In[12]:


df.T


# In[14]:


df.values


# In[15]:


df.dtypes


# In[19]:


df.shape


# In[20]:


df.info


# In[21]:


df.sum()


# In[22]:


df.max()


# In[28]:


df['语文'].max()


# In[29]:


df.describe()


# In[30]:


df.std()


# In[31]:


df.isnull()


# In[33]:


df = pd.read_excel('1月xlsx.xlsx')
df.head()


# In[36]:


df = pd.read_excel('1月xlsx.xlsx', sheet_name = 1)
df.head()


# In[42]:


df1 = pd.read_excel('1月xlsx.xlsx', index_col = 3)
df1.head()


# In[46]:



df1 = pd.read_excel('1月xlsx.xlsx', header = None)  # 列索引为数字
df1.head()


# In[55]:


df1[0].head()


# In[56]:


# 等同于
df1 = pd.read_excel('1月xlsx.xlsx', usecols = [0])
df1.head()


# In[61]:


# 导入CSV
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_csv('1月csv.csv', encoding = 'gbk')
df1.head()


# In[64]:


# 导入txt
df1 = pd.read_csv('1月txt.txt', sep = '\t', encoding = 'gbk')
df1.head()


# In[71]:


# 导入HTML
df = pd.DataFrame()
url_list = ['http://www.espn.com/nba/salaries/_/seasontype/4']
for i in range(2, 13):
    url = 'http://www.espn.com/nba/salaries/_/page/%s/seasontype/4'% i
    url_list.append(url)
for url in url_list:
    df = df.append(pd.read_html(url), ignore_index = True)
df = df[[x.startswith('$') for x in df[3]]]


# In[73]:


df.head()


# In[75]:


df.columns = ['index', 'name', 'team', 'salaries']


# In[76]:


df.head()


# In[77]:


df.to_csv('NBA.csv', index = False)


# In[78]:


# loc和iloc
data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
name = ['明日', '七月', '高', '二月']
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data = data, index = name, columns = columns)
df


# In[79]:


df.loc['明日']


# In[83]:


df.loc[['明日', '高']]


# In[85]:


df.iloc[[0, 2]]


# In[86]:


df.loc['明日': '二月']


# In[88]:


df.loc[:'高']


# In[89]:


df.iloc[0:4]


# In[90]:


df.iloc[:2]


# In[91]:


df.loc[:, ['语文', '数学']]


# In[94]:


df.iloc[:, [0, 1]]


# In[95]:


df.loc[:, '语文':]


# In[96]:


df.iloc[:, :2]


# In[98]:


print(df.loc['七月', '英语']) # 英语成绩
print(df.loc[['七月'], ['英语']])
print(df.loc[['七月'], ['数学', '英语']])


# In[99]:


df.iloc[[1], [2]]


# In[100]:


df.iloc[1:, [0, 2]]


# In[101]:


df.iloc[:, 2]


# In[102]:


df.loc[(df['语文'] > 105) & (df['数学'] > 88)]


# In[103]:


df['物理'] = [88, 79, 60, 50]


# In[104]:


df


# In[105]:


wl = [88, 34, 98, 100]
df.insert(2, '天文', wl)
df


# In[106]:


df.isnull()


# In[107]:


df.notnull()


# In[108]:


df.dropna(inplace = True)


# In[109]:


df


# In[115]:


df.loc['钱多多'] = [100, 120, 99,84, 34]


# In[116]:


df


# In[117]:


df.duplicated()


# In[119]:


df.drop_duplicates()


# In[120]:


# 索引设置
s1 = pd.Series([10, 20, 30], index = list("abc"))
s2 = pd.Series([2, 3, 4], index = list('bcd'))
s = s1+s2
s


# In[129]:


s1 = pd.Series([88, 60, 75], index = [1, 2, 3])
s1


# In[130]:


s1.reindex([1, 2, 3, 4, 5])


# In[132]:


s1.reindex([1, 2, 3, 4, 5], method = 'bfill')


# In[134]:


df = pd.DataFrame(pd.read_excel('mrbook.xlsx'))
df.head()


# In[136]:


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


# In[141]:


df = df.sort_values(by = '销量', ascending = False)
df


# In[146]:


df.sort_values(by = ['销量', '图书名称'], ascending = [False, True]).head()


# In[152]:


df1 = df.groupby(["类别"])["销量"].sum().reset_index()
df1


# In[153]:


df2 = df1.sort_values(by = '销量', ascending = False)
df2


# In[157]:


#dfrow.sort_values(by = 0, ascending = True, axis = 1)


# In[158]:


df = pd.DataFrame(pd.read_excel('mrbook.xlsx'))


# In[160]:


df = df.sort_values(by = '销量', ascending = False)
df['顺序排名'] = df['销量'].rank(method = "first", ascending = False)
df[['图书名称', '销量', '顺序排名']]


# In[166]:


df['平均排名'] = df['销量'].rank(ascending = False)
df


# In[167]:


df['销量'].rank(method = 'min', ascending = False)


# In[169]:


df['销量'].rank(method = 'max', ascending = False).reset_index()


# In[ ]:




