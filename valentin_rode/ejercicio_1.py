from sympy import *
from sympy.plotting import plot
from sympy.abc import x
import numpy as np

def energy_power(f):
    """
    Calculates the energy and power of a signal represented by the function `f(x)`.

    Arguments:
        f (function): Function that represents the signal. The function must be integrable in the interval [-∞, ∞].

    Returns:
        None: The function prints the energy and power of the signal to the console.
    """ 
    T=symbols("T")
    energia = integrate((abs(f)**2),(x,-oo, oo))
    potencia = limit((1/(2*T)*integrate(abs(f)**2,(x,-oo, oo))),T,oo)
    print("La energia de la señal es:",energia.evalf(3),"y su potencia es:",potencia.evalf(3))  

def piecewise_function():
#Defino la función pedida en manera simbólica
    f=Piecewise((0,x<=0),(x,x<=1),(2-x,x<2),(0,x>=2))
#Grafico la funcion
    f_graph=plot(f,show=True,xlim=(-10,10),ylim=(-2,5))
    return f
if __name__ == '__main__':
    f=piecewise_function()
    energy_power(f)
