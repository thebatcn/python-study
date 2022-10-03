from black import format_file_contents
import numpy as np
import pandas as pd

# pd.DataFrame对象使用reindex方法
frame = pd.DataFrame(
    np.arange(9).reshape(3, 3),
    index=["a", "c", "d"],
    columns=["Ohio", "Texas", "California"],
)

print(frame)

frame2 = frame.reindex(["a", "b", "c", "d"], method="ffill")  # reindex 行
print(frame2)

states = ["Texas", "Utah", "California"]

frame3 = frame.reindex(columns=states)  # 重新索引列
print(frame3)
print("\n")
# 弃某条轴上的一个或多个项很简单，只要有一个索引数组或列表即可
# drop方法返回的是一个在指定轴上删除了指定值的新对象
obj = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print(obj)
new_obj = obj.drop("c")  # drop 'c'行数据
print(new_obj)
print(obj.drop(["d", "c"], inplace=True))  # drop 'd'和'c'行数据,多行数据，带入列表。
# 使用inplace可以就地修改对象，不会返回新的对象
# 小心使用inplace，它会销毁所有被删除的数据。
print(obj)

# 对于DataFrame，可以删除任意轴上的索引值。
data = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["Ohio", "Colorado", "Utah", "New York"],
    columns=["one", "two", "three", "four"],
)
print(data)

# 用标签序列调用drop会从行标签（axis 0）删除值，默认axis0
print(data.drop(["Colorado", "Ohio"]))  # 删除行数据
print(data.drop("two", axis=1))  # 通过传递axis=1或axis=’columns’可以删除列的值
