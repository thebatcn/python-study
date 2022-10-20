from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np

frame = pd.DataFrame(
    np.arange(12.0).reshape((4, 3)),
    columns=list("bde"),
    index=["Utah", "Ohio", "Texas", "Oregon"],
)

serie = frame.iloc[0]

print(serie)
print(type(serie))
print(type(frame))
print(type(frame['b']))