import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

def secuencia():
    """
    Función que genera una secuencia aleatoria de 30 elementos, con amplitud entre 0 y 10.
    ------
    Returns: list
        Lista de la secuencia generada.
    """

    lista = [] 

    # Para un rango de 30 números genero un entero aleatorio entre 0 y 10.

    for i in range(30):
        numero = random.randint(0,11)
        lista.append(numero)
    
    return lista

def max_y_min(lista):
    """
    Encuentra los índices correspondientes a los valores máximos y mínimos de la secuencia.
    
    ------
    Parámetros:
    
    lista: list
        Lista de secuencia aleatoria generada, a la cual se le van a buscar los valores máximos y mínimos.

    ------
    Returns:

    minimo: int
        Valor mínimo de la lista
    
    posicion_min: list
        Lista de las posiciones en las cuales se encuentra el mínimo. 

    maximo: int
        Valor máximo de la lista
    
    posicion_max: list
        Lista de las posiciones en las cuales se encuentra el máximo.
    """
    # Búsqueda de valores máximos y mínimos.

    maximo = max(lista) 
    minimo = min(lista)

    indice_min = []
    indice_max = []

    # Búsqueda de las posiciones en las cuales se encuentran los máximos y minimos (considerando que pueden repetirse).

    for i in range(len(lista)):
        if lista[i] == minimo:
            indice_min.append(i+1)
        elif lista[i] == maximo:
            indice_max.append(i+1)


    return minimo, indice_min, maximo, indice_max

def graficar2(lista, min, max, min_posiciones, max_posiciones):
    """
    Grafica la secuencia obtenida, junto con los máximos y mínimos en su respectiva posición.

    ------
    Parámetros:

    lista: list
        Lista de secuencia aleatoria generada.
    
    min: int
        Valor mínimo de la lista

    max: int
        Valor máximo de la lista
    
    min_posiciones: list
        Lista de las posiciones en las cuales se encuentra el mínimo.    
    
    max_posiciones: list
        Lista de las posiciones en las cuales se encuentra el máximo.
    ------
    Returns: matplotlib plot
        Gráfico de la lista generada, junto con sus máximos y mínimos.     
    """

    # Definición de los dominios de las listas a graficar.

    dominio = np.arange(1,31)

    minimos = np.ones(len(min_posiciones)) * min
    dominio1 = min_posiciones

    maximos = np.ones(len(max_posiciones)) * max
    dominio2 = max_posiciones
    
    plt.stem(dominio, lista,"p", label="Lista Original")
    
    plt.stem(dominio1, minimos, "purple", label="Mínimos")

    plt.stem(dominio2, maximos, "green", label="Máximos")
    
    for i in range(len(dominio1)):
        plt.annotate(min, (dominio1[i], minimos[i]))

    for i in range(len(dominio2)):
        plt.annotate(max, (dominio2[i], maximos[i]))
    
    plt.title("Secuencia aleatoria con sus respectivos máximos y mínimos.")
    plt.xlabel("Muestras $n$")
    plt.ylabel("Amplitud")
    plt.grid()
    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":
    lista = secuencia()

    print(lista)

    min, indices_min, max, indices_max = max_y_min(lista)

    print("Valor Mínimo: ", min)
    print("Posiciones de los mínimos", indices_min)
    print("Valor Máximo: ", max)
    print("Posiciones de los máximos", indices_max)

    graficar2(lista,min,max,indices_min,indices_max)


