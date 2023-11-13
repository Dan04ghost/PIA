import numpy as np
primer_cuartil = np.percentile(datos, 25)
mediana = np.median(datos)
tercer_cuartil = np.percentile(datos, 75)
print(f"\nla mediana de los datos es igual a {mediana}")
print(f"el primer cuartil es igual a {primer_cuartil}, mientras que el tercer cuartil es igual a {tercer_cuartil}")
print(f"con rango intercuartil = {primer_cuartil} a {tercer_cuartil} o {tercer_cuartil - primer_cuartil}")
