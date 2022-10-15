import numpy as np
import pandas as pd

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])

print(s1 + s2)  # 自动的数据对齐操作在不重叠的索引处引入了NA值。缺失值会在算术运算过程中传播。
# a    5.2
# c    1.1
# d    NaN
# e    0.0
# f    NaN
# g    NaN
# dtype: float64

# DataFrame，对齐操作会同时发生在行和列上

df1 = pd.DataFrame(
    np.arange(9.0).reshape((3, 3)),
    columns=list("bcd"),
    index=["Ohio", "Texas", "Colorado"],
)
df2 = pd.DataFrame(
    np.arange(12.0).reshape((4, 3)),
    columns=list("bde"),
    index=["Utah", "Ohio", "Texas", "Oregon"],
)

#    b    c    d
# Ohio      0.0  1.0  2.0
# Texas     3.0  4.0  5.0
# Colorado  6.0  7.0  8.0
#
#  b     d     e
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0

print(df1 + df2)
#           b   c     d   e
# Colorado  NaN NaN   NaN NaN
# Ohio      3.0 NaN   6.0 NaN
# Oregon    NaN NaN   NaN NaN
# Texas     9.0 NaN  12.0 NaN
# Utah      NaN NaN   NaN NaN

#把它们相加后将会返回一个新的DataFrame，其索引和列为原来那两个DataFrame的并集