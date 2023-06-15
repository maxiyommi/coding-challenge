import matplotlib.pyplot as plt
import numpy as np

def graficar_sec(s, maximo, minimo, indice_maximo, indice_minimo):
    """grafica una secuencia aleatoria de números e indica su valor máximo y su valor mínimo en el gráfico"""
    x_vals = np.arange(len(s))  # Valores para el eje x con saltos de a uno

    # Graficar la secuencia de manera discreta
    plt.stem(x_vals, s, linefmt='b-', markerfmt='bo', basefmt=' ')

    # Marcar los puntos de máximo y mínimo
    plt.plot(indice_maximo, maximo, marker='o', color='red', label=f'Máximo: {maximo:.2f}')
    plt.plot(indice_minimo, minimo, marker='o', color='green', label=f'Mínimo: {minimo:.2f}')

    plt.title('Secuencia Aleatoria')
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Ajustar la posición de la leyenda fuera del gráfico
    plt.legend(loc='upper right', fontsize='x-small', bbox_to_anchor=(1.2, 1))

    # Establecer los valores y etiquetas de los ticks en el eje x con saltos de a dos
    plt.xticks(x_vals[::2])

    plt.show()
    return


    