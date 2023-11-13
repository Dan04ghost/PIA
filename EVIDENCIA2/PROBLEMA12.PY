import numpy as np
matrizA = np.random.randint(1,300, size=(5,10))
matrizB = np.random.randint(1,300, size=(5,10))

print(f"matriz A\n{matrizA}")
print("\nX\n")
print(f"matriz B\n{matrizB}")
print("\n=\n")
print(matrizA * matrizB)