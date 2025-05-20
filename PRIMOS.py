import time

start = time.time()

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primos = [n for n in range(1, 100001) if es_primo(n)]

# Imprimir la cantidad total
print(f"Cantidad total de primos encontrados: {len(primos)}")

end = time.time()
print(f"Tiempo de ejecución: {end - start:.2f} segundos")
print(f"{end - start:.6f}")
