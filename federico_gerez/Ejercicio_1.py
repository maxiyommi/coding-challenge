# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:53:32 2023

@author: Usuario
"""
import sympy
from sympy import symbols, Piecewise, integrate, limit
from sympy.plotting import plot

x, T = symbols('x T')

def funcion(x):
    """
    Define una función por tramos

    Parameters
    ----------
    x : Array
        Variable de entrada.

    Returns
    -------
    salida : Piecewise
        Función definida por tramos.

    """
    tramo_1 = 0
    tramo_2 = x
    tramo_3 = 2 - x
    tramo_4 = 0
    
    condiciones = [(tramo_1, x <= 0), (tramo_2, (x > 0) & (x <= 1)), (tramo_3, (x > 1) & (x < 2)), (tramo_4, x >= 2)]
    salida = Piecewise(*condiciones)
    sympy.pprint(salida)
    return salida

def graficar_funcion(salida):
    """
    Grafica una función definida por tramos

    Parameters
    ----------
    salida : Piecewise
        Función definida por tramos.

    Returns
    -------
    Grafico de la función

    """
    return plot(salida)



def energia_señal(señal):
    """
    Calcula la energia de una señal

    Parameters
    ----------
    señal : expresión simbólica
        señal de entrada.

    Returns
    -------
    energia : float
        energia de la señal.

    """
    energia = integrate(abs(señal)**2,(x, -sympy.oo, sympy.oo)).evalf()
    print("El valor de energia es: ", energia)
    return energia

def potencia_señal(señal):
    """
    Calcula la potencia promedio de una señal

    Parameters
    ----------
    señal : expresión simbolica
        señal de entrada.

    Returns
    -------
    potencia : float
        potencia promedio de la señal.

    """
    potencia = limit(1/(2*T)*integrate(abs(señal)**2,(x, -sympy.oo, sympy.oo)),T, sympy.oo)
    print("La potencia promedio es: ", potencia)
    return potencia

if __name__ == '__main__':
    salida = funcion(x)
    graficar_funcion(salida)
    energia_señal(salida)
    potencia_señal(salida)

