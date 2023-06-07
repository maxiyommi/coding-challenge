import numpy as np
import matplotlib.pyplot as plt

def graficar_secuencia_aleatoria():
    """
    Genera una secuencia aleatoria de 30 elementos con amplitud entre 0 y 10, 
    luego encuentra los valores máximos y mínimos, con la libreria numpy.
    Grafica la secuencia indicando los puntos máximos y mínimos con etiqueta y colores, 
    el color verde representa el valor maximo y el rojo el valor minimo.
    Esto mediante la libreria matplotlib.

    No tiene argumentos de entrada ni salida. La secuencia y su gráfico se generan directamente en la función.
    """
    # Generar secuencia aleatoria de 30 elementos entre 0 y 10
    secuencia = np.random.uniform(0, 10, 30)
    elementos = np.arange(len(secuencia))

    # Encontrar índices de los valores máximos y mínimos de la secuencia creada anteriormente
    indice_max = np.argmax(secuencia)
    indice_min = np.argmin(secuencia)

    # Obtener los valores máximos y mínimos
    maximo = secuencia[indice_max]
    minimo = secuencia[indice_min]

    # Graficar la secuencia con los máximos y mínimos
    plt.stem(elementos, secuencia)
    plt.plot(indice_max, maximo, marker='o', color='green', label='Máximo')
    plt.plot(indice_min, minimo, marker='o', color='red', label='Mínimo')
    plt.legend()

    # Etiquetas y leyendas
    plt.xlabel('Elementos')
    plt.ylabel('Amplitud')
    plt.title('Secuencia aleatoria indicando máximo y mínimo')

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    graficar_secuencia_aleatoria()
