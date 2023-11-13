import numpy as np
arreglo_uni = np.array([1,2,3,4,5,6,7,8,9])
filtro = arreglo_uni < 5
print(filtro)
resultado = arreglo_uni[filtro]
print()
print(resultado)