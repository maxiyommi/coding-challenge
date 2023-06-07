# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:34:51 2023

@author: Agustín
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def ejercicio2():
    lista = np.random.randint(10, size=(30))
    maximo = max(lista)
    minimo = min(lista)
    indices_max= []
    indices_min = []
    max_secuencia = []
    min_secuencia = []
    for i in range(len(lista)):
        if lista[i] == maximo:
            indices_max.append(i)
            max_secuencia.append(maximo)
            min_secuencia.append(None)
        elif lista[i] == minimo:
            indices_min.append(i)
            min_secuencia.append(minimo)
            max_secuencia.append(None)
        else:
            min_secuencia.append(None)
            max_secuencia.append(None)
    print(maximo)
    print(lista[indices_max[0]])
    grafico_ej2(lista,max_secuencia,min_secuencia)
    return maximo, minimo, indices_max,indices_min
    
def grafico_ej2(lista,max_secuencia,min_secuencia):
    plt.title("Ejercicio 2")
    plt.stem(lista)
    plt.stem(max_secuencia, linefmt="k--", label="maximos")
    plt.stem(min_secuencia, linefmt="g:", label="minimos")
    plt.legend()
    plt.show()
    plt.figure()
    
if __name__ == "__main__":
    valor_max, valor_min, ind_max, ind_min = ejercicio2()
    print("los indices con el valor maximo (", valor_max, "), son: ", ind_max)
    print("los indices con el valor minimo (", valor_min, "), son: ", ind_min)
