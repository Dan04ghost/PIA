import pandas as pd
import numpy as np
from math import log

s = pd.Series([1,2,3,4])
print(s.apply(log))

s = pd.Series(['a','b','c'])
print(s.apply(str.upper))

s = pd.Series({'matematicas': 6.0, 'economia': 4.5, 'programacion': 8.5})
print(s[s > 5])
print(s.sort_values())
print(s.sort_index(ascending=False))

s = pd.Series(['a','b',None,'c',np.nan,'d'])
print(s)
print(s.dropna())