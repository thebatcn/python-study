import pandas as pd

data = {
    "state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
    "year": [2000, 2001, 2002, 2001, 2002, 2003],
    "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
}

frame = pd.DataFrame(data)

print(pd.DataFrame(data, columns=["year", "state", "pop"]))
# 如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列

frame2 = pd.DataFrame(
    data,
    columns=["year", "state", "pop", "debt"],
    index=(["one", "two", "three", "four", "five", "six"]),
)  # 重新设置索引
print(frame2)
# 如果传入的列在数据中找不到，就会在结果中产生缺失值

# print(frame2.columns)   #列名称
# print(frame2.index  )   #索引
# print(frame2['pop'])    #通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
#
# print(frame2.loc['six'])   #行也可以通过位置或名称的方式进行获取，比如用loc属性

# 列可以通过赋值的方式进行修改
frame2["debt"] = 15.5
# print(frame2)

# 将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配。如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有的空位都将被填上缺失值
val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])
frame2["debt"] = val
# print(frame2)

# 为不存在的列赋值会创建出一个新列。关键字del用于删除列

frame2["eastern"] = frame2["state"] == "Ohio"
# print(frame2)

del frame2["eastern"]
print(frame2)

#如果嵌套字典传给DataFrame，pandas就会被解释为：外层字典的键作为列，内层键则作为行索引
pop = {'Nevada':{2001:2.4,2002:2.9},'Ohio:':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = pd.DataFrame(pop)
print('\n',frame3)

# print(frame3.T)
#你也可以使用类似NumPy数组的方法，对DataFrame进行转置（交换行和列）

#内层字典的键会被合并、排序以形成最终的索引。如果明确指定了索引，则不会这样
#合并，排序提现在哪里？
# print(pd.DataFrame(pop,index=[2001,2002,2003]))
# print(pop)
# pdata = {'Ohio':frame3['Ohio'][:-1],            #取列数据0至-1，到倒数第二个
        #  'Nevada':frame3['Nevada'][:2]}         #取1和2两个数
# print(pdata)      
# frame3.index.name='year';frame3.columns.name='state'
# print(frame3)   
# 如果设置了DataFrame的index和columns的name属性，则这些信息也会被显示出来
# 
# obj = pd.Series(range(3),index=['a','b','c'])
# index = obj.index
# print(type(index))
# 
# index[1]='d'    #index对象元素不能修改？对象可以整体赋值？
# index = ['x','y','z']  #变成了 list，其他类型了。
# print(type(index))
# 
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

obj2 = obj.reindex(['a','b','c','d','e'])   #用该Series的reindex将会根据新索引进行重排。如果某个索引值当前不存在，就引入缺失值
print(obj2)

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
obj3 = obj3.reindex(range(6),method="ffill")
#重新索引时可能需要做一些插值处理。method选项即可达到此目的，例如，使用ffill可以实现前向值填充
print(obj3)

