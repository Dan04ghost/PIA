import numpy as np
media = np.mean(datos)
desviacion_estandar = np.std(datos)
varianza = np.var(datos)
print(f"\nlos datos poseen una media aritmetica de {media: .4f}, con una varianza de {varianza: .4f} y una desvicion estandar de {desviacion_estandar: .4f}")
