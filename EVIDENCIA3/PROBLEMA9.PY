import pandas as pd
import numpy as np
from math import log
datos = {'nombre':['María', 'Luis', 'Carmen'],
'edad':[18, 22, 20],
'Matemáticas':[8.5, 7, 3.5],
'Economía':[8, 6.5, 5],
'Programación':[6.5, 4, 9]}
df = pd.DataFrame(datos)
df1 = df.melt(id_vars=['nombre', 'edad'], 
var_name='asignatura', value_name='nota')
print(df1)

print(df1.pivot(index='nombre', 
columns='asignatura', values='nota'))
