import numpy as np
math=np.array([101,109,115,108,118,118])
en=np.array([117,105,118,108,98,109])
total=np.array([621,623,620,620,615,615])
sort_total=np.lexsort((en,math,total))
print('排序后的索引值')
print(sort_total)
print ('通过排序后的索引获取排序后的数组：')
print(np.array([[en[i],math[i],total[i]] for i in sort_total]))
