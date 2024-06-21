
'''
Ejercicio_2
Utilizando Numpy,
1. Generar una secuencia aleatoria de 30 elementos, con amplitud entre 0 y 10.
2. Encontrar los índices correspondientes a los valores máximos y mínimos de la secuencia
3. Graficar la secuencia con los máximos y mínimos en un mismo gráfico, indicando con leyendas y etiquetas que representan.
'''

import numpy as np
import matplotlib.pyplot as plt

def secuencia():

    # 1.
    secuencia = np.random.uniform(0, 10, 30)

    # 2. 
    minimo = np.argmin(secuencia)
    maximo = np.argmax(secuencia)

    # 3. 
    plt.plot(secuencia, marker = 'o', label = 'Secuencia Aleatoria')
    plt.plot(maximo, secuencia[maximo], 'yx', label='Máximo')
    plt.plot(minimo, secuencia[minimo], 'rx', label='Mínimo')
    plt.xlabel('Elementos')
    plt.ylabel('Amplitud')
    plt.title('Secuencia Aleatoria con Máximos y Mínimos')
    plt.legend()
    plt.grid(True)
    plt.show()

    return secuencia