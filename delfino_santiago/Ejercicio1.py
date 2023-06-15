# -*- coding: utf-8 -*-
"""
La función devuelve la salida simbólica de una función a trozos de variable x. 
Y la gráfica de una función 
---------
x: variable inicializada
trozos: Se definen de forma simbólica los trozos de la función
funcion_a_trozos: A partir del metodo de sympy Piecewise se genera la función a trozos
funcion_partida: Devuelve un sp.print
graficar_funcion: Devuelve un plot con el metodo splt.plot de sympy plotting


    
"""

import sympy as sp
import sympy.plotting as splt


# Definir la variable simbólica
x = sp.Symbol('x')


def funcion_partida(x):
    # Definir los trozos de la función
    trozos = [(0, x <= 0), (x, (x > 0) & (x <= 1)), (2-(x), (x > 1) & (x < 2)), (0, x >= 2)]
    
    # Crear la función a trozos
    funcion_a_trozos = sp.Piecewise(*trozos)
    resultado = sp.pprint(funcion_a_trozos)
    return resultado
funcion_partida(x)

def graficar_funcion(funcion_a_trozos):
    trozos = [(0, x <= 0), (x, (x > 0) & (x <= 1)), (2-(x), (x > 1) & (x < 2)), (0, x >= 2)]
    
    # Crear la función a trozos
    funcion_a_trozos = sp.Piecewise(*trozos)
    return splt.plot(funcion_a_trozos)

funcion_a_trozos = funcion_partida(x)
graficar_funcion(funcion_a_trozos)

if __name__ == "__main__":
    
    f_p = funcion_partida(x)
    g_f = graficar_funcion(funcion_a_trozos)