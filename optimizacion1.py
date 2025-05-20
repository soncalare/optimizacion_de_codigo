import time
import numpy as np

start = time.time()

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # Solo impares
        if n % i == 0:
            return False
    return True

# Crear un array NumPy con números del 1 al 100000
numeros = np.arange(1, 100001)

# Filtrar usando list comprehension con NumPy para eficiencia
primos = np.array([n for n in numeros if es_primo(n)])

# Imprimir resultados
print(f"Cantidad total de primos encontrados: {len(primos)}")
print(f"Primeros 10 primos: {primos[:10]}")

end = time.time()
print(f"Tiempo de ejecución: {end - start:.2f} segundos")
