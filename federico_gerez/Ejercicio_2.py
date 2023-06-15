# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:27:04 2023

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

def secuencia_aleatoria(n):
    """
    Genera una secuencia de numeros entre 0 y 10

    Parameters
    ----------
    n : int
        longitud de la secuencia.

    Returns
    -------
    secuencia : numpy array
        secuencia aleatoria de números.

    """
    secuencia = 10 * np.random.rand(n)
    print(secuencia)
    return secuencia

def indice_max_min(secuencia):
    """
    Encuentra los indices correspondientes al valor máximo y mínimo de una secuencia

    Parameters
    ----------
    secuencia : numpy array
        secuencia aleatoria de números.

    Returns
    -------
    indice_maximo : int
        indice del valor máximo de la secuencia.
    indice_minimo : int
        indice del valor mínimo de la secuencia.

    """
    indice_maximo = np.argmax(secuencia)
    indice_minimo = np.argmin(secuencia)
    
    print("Índice del valor máximo:", indice_maximo)
    print("Índice del valor mínimo:", indice_minimo)
    
    return indice_maximo, indice_minimo

def graficar_secuencia(secuencia, indice_maximo, indice_minimo):
    """
    Grafica una secuencia con los valores máximo y mínimo resaltados

    Parameters
    ----------
    secuencia : numpy array
        secuencia aleatoria de números.
    indice_maximo : int
        indice del valor máximo de la secuencia.
    indice_minimo : int
        indice del valor mínimo de la secuencia.

    Returns
    -------
    Grafico de la secuencia con los valores máximo y mínimo resaltados.

    """
    plt.plot(secuencia, label='Secuencia')
    plt.scatter(indice_maximo, secuencia[indice_maximo], color='red', label='Máximo')
    plt.scatter(indice_minimo, secuencia[indice_minimo], color='green', label='Mínimo')

    # Etiquetas y leyenda
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Secuencia con máximos y mínimos')
    plt.legend()

    return plt.show()

if __name__ == '__main__':
    secuencia = secuencia_aleatoria(30)
    indice_maximo, indice_minimo = indice_max_min(secuencia)
    graficar_secuencia(secuencia, indice_maximo, indice_minimo)
