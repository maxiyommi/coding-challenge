# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:44:52 2023

@author: Franco
"""
import numpy as np
import matplotlib.pyplot as plt

def secuencia_aleatoria():
    """
    Función que genera una secuencia de 30 valores aleatorios con amplitud entre 0 y 10, calcula sus mínimos y máximos y extrae los índices en donde estos se encuentran dentro de la secuencia.
    Además grafica la secuencia con sus máximos y mínimos destacados en el mismo gráfico.
    Utiliza numpy para generar la secuencia y matplotlib para realizar el gráfico.
    Parámetros:
    *secuencia: secuencia aleatoria
    *minimo, maximo: valores mínimos y máximos
    *indexmin, indexmax: índices de valores mínimos y máximos
    
    La función no requiere argumentos de entrada o salida.
    """
    secuencia = np.random.randint(0,10,30)
    minimo = min(secuencia)
    maximo = max(secuencia)
    indexmin = []   
    indexmax = []
    
    for n in range(len(secuencia)):
        if secuencia[n] == minimo:
            indexmin.append(n)
        elif secuencia[n] == maximo:
            indexmax.append(n)
        else:
            pass
        
    plt.stem(np.arange(0,30),secuencia,'r',label="Secuencia")
    plt.title('Secuencia de valores aleatorios')
    plt.ylabel("Amplitud")
    plt.xlabel("Indice")
    plt.stem(indexmin,secuencia[indexmin],'y',label = "Minimos")
    plt.stem(indexmax,secuencia[indexmax],'b', label = "Maximos")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    secuencia_aleatoria()
   