import numpy as np
import pandas as pd

# Series索引（obj[…]）的工作方式类似于NumPy数组的索引，只不过Series的索引值不只是整数。下面是几个例子：

obj = pd.Series(np.arange(5.0), index=["a", "b", "c", "d", "e"])
print(obj)
print(obj["b"])  # 选取'b'行，就1行，从0开始的。
print(obj[2:4])  # a[2]和[3]，同列表一致，不包含右端值。
print(obj[["b", "a", "d"]])  # 选择多个用列表值
print(obj[[1, 3]])  # 用系统数字索引。第2行，第4行。
print(obj[obj < 2])  # 根据条件,obj数字小于2.

# 利用标签的切片运算与普通的Python切片运算不同，其末端是包含的
print(obj["b":"c"])  # 包含'b'和'c'行

obj["b":"c"] = 5  # 用切片可以对Series的相应部分进行设置
print(obj)

# 用一个值或序列对DataFrame进行索引其实就是获取一个或多个列
# 选取的是列，要选行用下面方法。
data = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["Ohio", "Colorado", "Utah", "New York"],
    columns=["one", "two", "three", "four"],
)

data1 = data.copy()
print(data)
print(data['two'])

# obj[:2]选取的是行，0-1行。obj[2:3]是[2]行。如果列和行索引都设置一样名称，就可以看出obj[2]选取的是列[2]。
#    1  2  3
# 1  0  1  2
# 2  3  4  5
# 3  6  7  8

#另一种用法是通过布尔型DataFrame（比如下面这个由标量比较运算得出的）进行索引
print(data<5)  #比较标量，得到一个布尔值DataFrame对象
data[data<5] =0  #赋值，True的标量设置为0.
print(data)
#这使得DataFrame的语法与NumPy二维数组的语法很像。

# DataFrame的行的标签索引，我引入了特殊的标签运算符loc和iloc。
# 它们可以让你用类似NumPy的标记，使用轴标签（loc）或整数索引（iloc），从DataFrame选择行和列的子集
#           one   two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

print('\n',data1)
print(data1.loc['Utah',['two','three']])        #'Utah'行，列'two','three'的2个值：9,10
print(data1.iloc[[2,0],[3,0,1]])                    #[2][0]行，[3,0,1]列交叉的值：11,8,9,3,0,1

print(data1.loc[:'Utah', 'two'])                #['Ohio']--['Utah']行，'two'列交叉值 1，5,9
print(data1)

print(data1.iloc[:,:3])                          #所有行。:3表示0，1,2列
print(data1.iloc[:, :3][data1.three > 5])        #根据 data1.three >5 ,截取了three列数据。前面one\two列数据舍弃，对齐three.

data1['three']=[2,4,10,14]                      #重新赋值three列数值，验证one\two数据对齐
print(data1)
print(data1.iloc[:, :3][data1.three > 5])  