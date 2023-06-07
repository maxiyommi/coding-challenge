# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:27:54 2023

@author: Martin
"""

import sympy as sym
from sympy.plotting import plot
from sympy import limit, integrate
# importo librerias

def Fun_1 ():
    """
    La funcion crea una funcion f(x) por partes usando Piecewise, la grafica, 
    y calcula la energia y la potencia, devolviendo los valores obtenidos.
    """
    
    # Defino la variable simbolica
    x = sym.symbols ("x") 

    # Expreso la funcion por partes usando Piecewise
    funcion = sym.Piecewise ((0, x <= 0), (x, (0 < x) & (x <= 1)), (2 - x, (1 < x) & (x < 2 )),(0, x >= 2))
    
    #Grafico la funcion
    g = plot(funcion, show = False)

    g.title = "Funcion Simbolica"
    g.xlabel = "x"
    g.ylabel = "f(x)"
    g.xlim = -1,4
    g.ylim = -1,2
    g.show()
    
    #Calculo la energia total de la funcion
    E = limit(integrate(abs(funcion)**2,(x, -sym.oo, sym.oo)), x, sym.oo)
    
    #Calculo la potencia promedio de la funcion
    P = limit((1/(2*x)*integrate(abs(funcion)**2,(x,-sym.oo, sym.oo))),x,sym.oo)
    
    #Imprimo los valores de Energia y Potencia
    a = print("La potencia promedio es = ", P.evalf())
    b = print("La energia total es = ", E.evalf())
    return (a,b)



