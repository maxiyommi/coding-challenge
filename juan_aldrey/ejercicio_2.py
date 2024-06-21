import numpy as np
import matplotlib.pyplot as plt

randomSequence = np.random.uniform(0, 10, 30)

print("La secuencia aleatoria: ", randomSequence)

maxIndex = np.argmax(randomSequence)
minIndex = np.argmin(randomSequence)

print("Índice del máximo: ", maxIndex)
print("Índice del mínimo: ", minIndex)

plt.figure(figsize=(10, 6))
plt.plot(randomSequence, marker='o', linestyle='-', color='b', label='Random Sequence')
plt.scatter(maxIndex, randomSequence[maxIndex], color='red', label=f'Maximum ({randomSequence[maxIndex]:.2f})', s=100, zorder=3)
plt.scatter(minIndex, randomSequence[minIndex], color='green', label=f'Minimum ({randomSequence[minIndex]:.2f})', s=100, zorder=3)
plt.title('Secuencia aleatoria con valores máximos y mínimos')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()