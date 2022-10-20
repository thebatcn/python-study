import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),columns=list('abcd'))

print(df1)
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),columns=list('abcde'))

print(df2)

print(df2.loc[1,'b'])
df2.loc[1,'b'] = np.nan
print(df2)

df3=df1+df2
df3.loc[1,"b"]=6.0
print('df2','\n',df2)
print('df3','\n',df3)
print('df3+df2','\n',df3.add(df2,fill_value=1))
#Nan项+如何值都等于Nan，前面有讲解？
#就是说对于对于只在一个DataFrame中缺#失的位置会被替换成我们指定的值，如果#在两个DataFrame都缺失，那么依然还会#是Nan。

arr = np.arange(12.).reshape(3,4)
print(arr)
print(arr[0])
print(arr-arr[0])
#   [[ 0.  1.  2.  3.]
#   [ 4.  5.  6.  7.]
#   [ 8.  9. 10. 11.]]

#   [0. 1. 2. 3.]

#   [[0. 0. 0. 0.]
#   [4. 4. 4. 4.]
#   [8. 8. 8. 8.]]

# 当我们从arr减去arr[0]，每一行都会执行这个操作。这就叫做广播（broadcasting）