# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:13:46 2023

@author: Franco
"""

import sympy as sym
import matplotlib.pyplot as plt

def funcion_simbolica():
    """
    Función que escribe a f(x) de forma simbolica, realiza el gráfico de la misma y calcula e informa los valores de energía total y potencia promedio de f(x)
    Utiliza sympy como método simbólico y matplotlib para realizar el gráfico.
    Parámetros:
    *x, T : variables temporales
    *f : función f(x)
    *E : energia total
    *P : potencia promedio
    
    La funcion no requiere de argumentos de entrada ni salida
    """
    x, T = sym.symbols('x T')
    f = sym.Piecewise((0,x<=0),(x,(x>0)&(x<=1)),(2-x,(x>1)&(x<2)),(0,x>=2))
    sym.plot(f,(x,-5,5),line_color='black', title='Función ejercicio', xlabel='tiempo', ylabel='f(x)')
    E = sym.integrate(abs(f)**2,(x,0,2))
    P = sym.limit(((1/2*T)*sym.integrate(abs(f)**2,(x,-sym.oo,sym.oo))),T,sym.oo)
    print("El valor de energía para esta función es de: ", E)
    print("El valor de potencia promedio de esta función es de :",P)
    

if __name__ == "__main__":
    funcion_simbolica()


