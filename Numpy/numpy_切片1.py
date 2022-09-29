import numpy as np
"""numpy array于与list切片赋值"""
nl=np.arange(10)
lst=[x for x in range(10)]
print('lst:',lst)
 
nl[5:8]=12
print('nl: ',nl)
lst[5:8]=[12,12,12,13] #只能是序列，个数不一致，多余按等于插入操作
print('lst:',lst)
print('len(lst):',len(lst))
lst[5:8]=[12,12] #少于按删除？
print('lst:',lst)
print('len(lst):',len(lst))