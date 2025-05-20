import matplotlib.pyplot as plt

# Tiempos medidos manualmente (cámbialos por los reales)
tiempos = [3.42, 1.12]  # [original, optimizado]
etiquetas = ['Original', 'Optimizado']

plt.bar(etiquetas, tiempos, color=['red', 'green'])
plt.title("Comparación de tiempos de ejecución")
plt.ylabel("Tiempo (segundos)")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Simulación de 20 mediciones
original = np.random.normal(loc=3.5, scale=0.1, size=20)
optimizado = np.random.normal(loc=1.1, scale=0.05, size=20)

plt.hist(original, alpha=0.6, label='Original', bins=10, color='red')
plt.hist(optimizado, alpha=0.6, label='Optimizado', bins=10, color='green')
plt.title("Distribución de tiempos de ejecución")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()
