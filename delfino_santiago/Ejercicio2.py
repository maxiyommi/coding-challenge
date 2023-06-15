# -*- coding: utf-8 -*-
"""

La función devuelve un array de 30 elementos aleatorios con valores 
de amplitud entre 0 y 10, su valor máximo y mínimo. Además nos da información respecto a 
los índices de los máximos y mínimos en la secuencia
---------
secuencia: array con los valores 
maximo_secuencia: Mediante el metodo max de Numpy devuelve el valor máximo del array
minimo_secuencia: Mediante el metodo min de Numpy devuelve el valor máximo del array
locacion_maximo: Devuelve con el metodo where de Numpy el array de indices donde esta el valor maximo
locacion_minimo: Devuelve con el metodo where de Numpy el array de indices donde esta el valor minimo
salida: Devuelve en valores discretos la variable secuencia    
    

"""

import numpy as np
import matplotlib.pyplot as plt

secuencia = np.random.randint(0,11,size=30)
def valores_aleatorios(secuencia):
    maximo_secuencia = np.max(secuencia)
    minimo_secuencia = np.min(secuencia)
    locacion_maximo = np.where(secuencia == np.max(secuencia))
    locacion_minimo = np.where(secuencia == np.min(secuencia))


    print(secuencia)
    print(maximo_secuencia)
    print(minimo_secuencia)
    print(locacion_maximo)
    print(locacion_minimo)
    salida=plt.stem(secuencia)
    plt.title("Secuencia aleatoria")
    plt.xlabel("Valores de entrada aleatorios")
    plt.ylabel("Salidas aleatorias")
    return secuencia, maximo_secuencia, minimo_secuencia, locacion_maximo, locacion_minimo, salida 

valores_aleatorios(secuencia)


if __name__ == "__main__":
    
    v_a = valores_aleatorios(secuencia)

        
