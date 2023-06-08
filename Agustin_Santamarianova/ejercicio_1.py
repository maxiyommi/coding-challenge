# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:36:48 2023

@author: Agustín
"""

import sympy
from sympy.interactive import printing
printing.init_printing(use_latex='mathjax')
from IPython.display import display
from sympy import limit, integrate
import matplotlib.pyplot as plt
from sympy.plotting import plot

def ejercicio1():
    x = sympy.symbols("x")
    expr1=0
    expr2 = x
    expr3= 2-x
    
    funcion = sympy.Piecewise((expr1, x <= 0), (expr2,(x>0) & (x <= 1)), (expr3,(x>1) & (x<2)), (expr1, x>=2))
    E =  integrate(abs(funcion)**2,(x,-sympy.oo, sympy.oo))
    E = E.doit()
    P = limit((1/(2*x)*integrate(abs(funcion)**2,(x,-sympy.oo, sympy.oo))),x,sympy.oo)
    plot(funcion, title="Ejercicio 1")
    return funcion,E,P

    
    
    
if __name__ == "__main__":
    Funcion,Energia,Potencia = ejercicio1()
    display(Funcion)
    print ("La energía es: ",Energia) 
    print("La potencia es: ", Potencia)