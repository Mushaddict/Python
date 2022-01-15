import pandas as pd
s1=pd.Series([88,60,75], index = [1, 2, 3])
s2 = pd.Series([20, 34, 24], index = [2, 3, 4])
# s = s1 + s2
# print(s)
# # print(s1)
print(s1[1])
print(s1[[1, 2]])

