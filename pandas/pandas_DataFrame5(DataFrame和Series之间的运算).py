from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np

frame = pd.DataFrame(
    np.arange(12.0).reshape((4, 3)),
    columns=list("bde"),
    index=["Utah", "Ohio", "Texas", "Oregon"],
)

        #   b     d     e
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0

serie = frame.iloc[0]

print(serie)
# b    0.0
# d    1.0
# e    2.0
# Name: Utah, dtype: float64
print('serie',type(serie))          #Series   DateFrames的行数据
print(type(frame))          #DateFrame
print(type(frame['b']))     #Series  DateFrames的列，是Series。
print('frame[b]',frame['b'])

frame - serie
#         b    d    e
# Utah    0.0  0.0  0.0
# Ohio    3.0  3.0  3.0
# Texas   6.0  6.0  6.0
# Oregon  9.0  9.0  9.0

# 默认情况下，DataFrame和Series之间的算术运算会将Series的索引匹配到DataFrame的列，然后沿着行一直向下广播：

series2 = frame['d']
print(series2)

# Utah       1.0
# Ohio       4.0
# Texas      7.0
# Oregon    10.0
# Name: d, dtype: float64
print(frame - series2)    #series2的索引，运算时匹配到frame的列了，没有重叠的就取并集,值为NaN。
#         Ohio  Oregon  Texas  Utah   b   d   e
# Utah     NaN     NaN    NaN   NaN NaN NaN NaN
# Ohio     NaN     NaN    NaN   NaN NaN NaN NaN
# Texas    NaN     NaN    NaN   NaN NaN NaN NaN
# Oregon   NaN     NaN    NaN   NaN NaN NaN NaN

frame.sub(series2, axis='index')

#           b    d    e
# Utah   -1.0  0.0  1.0
# Ohio   -1.0  0.0  1.0
# Texas  -1.0  0.0  1.0
# Oregon -1.0  0.0  1.0

#传入的轴号就是希望匹配的轴。在本例中，我们的目的是匹配DataFrame的行索引（axis=‘index’ or axis=0）并进行广播。