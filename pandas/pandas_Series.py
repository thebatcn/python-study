import pandas as pd
 
obj = pd.Series([1,2,3,4])
print(obj)
print(obj.values)
print(obj.index)
 
obj1 = pd.Series([5,6,7,8],index=['a','b','c','d'])
print(obj1)
print(obj1.index)
print(obj1['b'])
print(obj1[3])
oo=obj1>5
print(type(oo))
print(oo)
print(obj1[obj1>5])
#果只传入一个字典，则结果Series中的索引就是原字典的键（有序排列）
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj2 = pd.Series(sdata)
print(obj2)
print(obj2.index)
#你可以传入排好序的字典的键以改变顺序
states =['a','Utah','b','c']
obj3 = pd.Series(sdata,index=states)
print(obj3)
print(obj3.index)
#这个例子中，sdata中跟states索引相匹配的那3个值会被找出来并放到相应的位置上，但由于“California”所对应的sdata值找不到，所以其结果就为NaN（即“非数字”（not a number），在pandas中，它用于表示缺失或NA值）。y
 
#对于许多应用而言，Series最重要的一个功能是，它会根据运算的索引标签自动对齐数据
o23=(obj2 + obj3)
print(o23)
print(o23.isnull())
#Series对象本身及其索引都有一个name属性，该属性跟pandas其他的关键功能关系非常密切
print(o23.name)
o23.name = 'population'
o23.index.name = 'state'
print(o23)
#Series的索引可以通过赋值的方式就地修改
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)