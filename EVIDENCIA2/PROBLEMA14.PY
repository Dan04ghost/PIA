import numpy as np
matriz_ejemplo = np.random.randint(1,300, size=(2,5))
print(matriz_ejemplo)
print()
filtro = matriz_ejemplo > 100
print(filtro)
print()
resultado = matriz_ejemplo[filtro]
print(resultado)