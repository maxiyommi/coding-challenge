import numpy as np
import matplotlib.pyplot as plt



# Ejercicio 2

# Generar secuencia aleatoria de 30 elementos entre 0 y 10 por medio de np.random
secuencia = np.random.uniform(0, 10, size=30)
###### Intenté resolver los valores máximos y mínimos con el código a continuación, sin embargo me seguía arrojando un error

# max_random = max(secuencia)
# posicion_maximo = secuencia.index(max_random)
# print(posicion_maximo)

###### Decidí resolver con argmax() y argmin() de la librería Numpy

# Encontré el índice del valor máximo
indice_maximo = np.argmax(secuencia)

# Encontré el índice del valor mínimo
indice_minimo = np.argmin(secuencia)
print(secuencia)
print("Índice del valor máximo:", indice_maximo)
print("Índice del valor mínimo:", indice_minimo)
print("Recordar que las posiciones de ésta secuencias se comienzan a contar empezando con la posición 0 siendo el primer valor de la secuencia")
# Grafico la secuencia
plt.stem(secuencia)
plt.xlabel('Posición')
plt.ylabel('Valor de Amplitud')
plt.title('Gráfico de la Secuencia')
plt.grid(True)
plt.show()
