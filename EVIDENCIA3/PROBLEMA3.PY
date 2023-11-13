import pandas as pd
s = pd.Series([1,2,2,3,3,3,4,4,4,4])
print(s.size)
print(s.index)
print(s.dtype)

print(s[1:3])