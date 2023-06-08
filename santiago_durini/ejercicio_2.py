import numpy as np
import matplotlib.pyplot as plt

def ej2():
    """
    Esta función genera una secuencia aleatoria de 30 elementos y encuentra los índices
    correspondientes a los valores máximos y mínimos de la secuencia.
    ---
    Devuelve:
        a: array
            La secuencia aleatoria de 30 elementos.
        indice_max: lista
            Los índices correspondientes a los valores máximos de la secuencia.
        indice_min: lista
            Los índices correspondientes a los valores mínimos de la secuencia.
    """

    a = np.random.randint(0, 10, size=30)
    minimo = min(a)
    indice_min = []
    for n in range(len(a)):
        if a[n] == minimo:
            indice_min.append(n)
        else:
            pass
    maximo = max(a)
    indice_max = []
    for n in range(len(a)):
        if a[n] == maximo:
            indice_max.append(n)
        else:
            pass

    return a, indice_max, indice_min

def grafico_2(array,indice_max,indice_min):
    """
    Esta función grafica una secuencia junto con los índices correspondientes a los valores máximos
    y mínimos de la secuencia.
    ---
    Parametros:
        array: array
            La secuencia de valores.
        indice_max: lista
            Los índices correspondientes a los valores máximos de la secuencia.
        indice_min: lista
            Los índices correspondientes a los valores mínimos de la secuencia.
    """
    n = np.arange(0, 30)
    plt.stem(n, array, 'b', label='Secuencia aleatoria')
    plt.stem(indice_max, array[indice_max], 'r', label='Maximos')
    plt.stem(indice_min, array[indice_min], 'g', label='Minimos')
    plt.title('Secuencia aleatoria')
    plt.ylabel('Valor')
    plt.xlabel('Muestras')
    plt.legend(loc='upper right')
    plt.grid()

    plt.show()