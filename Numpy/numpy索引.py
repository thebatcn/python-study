import numpy as np
 
 
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
#布尔型索引
#arr= np.random.randn(7,4)
#print(arr,'\n')
#print(arr>0,'\n')
#arr[arr<0]=0
#print(arr,'\n')
 
#a = arr[names=='Bob']
#print(a)
 
#b = names!='Bob'
#print(b)
 
#print('\n',arr[b])
#print('\n',arr[names!='Bob'])
 
#arr = np.empty((8, 4))
#for i in range(8):
#   arr[i]=i
#花式索引
#print(arr,'\n')
#print(arr[[4,0,2,-1,-4]])
 
#reshape方法
arr=np.arange(32).reshape(4,8)
print(arr,'\n')
print(np.reshape(arr,32),'\n')
print(arr.reshape(16,2))