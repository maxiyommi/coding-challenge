import random
import matplotlib.pyplot as plt

secuencia_aleatoria = []
for i in range(30):
    int_random = random.randint(0, 10)
    secuencia_aleatoria.append(int_random)

maximo = max(secuencia_aleatoria)
minimo = min(secuencia_aleatoria)

print(secuencia_aleatoria)
print("Valor máximo: ", maximo)
print("Valor minimo: ", minimo)

fig, ax = plt.subplots()
indices = range(len(secuencia_aleatoria))
plt.vlines(indices, ymin=0, ymax=secuencia_aleatoria, color='b', linewidth=2)
ax.set_xlabel('Índice')
ax.set_ylabel('Valor')
ax.set_title('Gráfico tipo fósforo de secuencia aleatoria')
plt.grid(True)
plt.tight_layout()
plt.show()

