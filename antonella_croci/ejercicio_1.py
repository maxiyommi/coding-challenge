import sympy as sym
from sympy.plotting import plot
from sympy import integrate, limit
import numpy as np
from IPython.display import display

def funcion():
    """
    Dada una función continua, la expresa de manera simbólica.

    ------
    Returns:
    x: sym
        Símbolo de la variable independiente.
    fx: Función simbólica.
        Función simbólica expresada a trozos.

    """
    x = sym.symbols('x') # Convierte a la variable x en un símbolo

    f = sym.Piecewise((0, x<=0),(x, (x>0)&(x<=1)),(2-x, (x>1)&(x<2)),(0, (x>=2))) # Definición de la función a trozos

    return x, f

def graficar(fx):
    """
    Función que recibe una función de manera simbólica junto con su dominio y la grafica. 
    ------
    Parámetros:

    fx: 
        Función expresada de manera simbólica.
    ------
    Returns: sympy plot
        Gráfico de la expresión simbólica.
    """

    plot(fx, title="Gráfico de f(x)", xlabel="$x$",ylabel="$f(x)$",xlim=(-5,5), ylim=(0,1)) # Grafica la función



def energia_potencia(x, fx):
    """
    Función para el cálculo de la energía y de la potencia de una función.

    ------
    Parámetros:
    x: sym
        Símbolo de la variable independiente. 
    
    fx: Función simbólica
        Función simbólica de la cual se quiere obtener la energía y potencia. 

    ------
    Returns: 
    e: float
        Energía de la función.
    p: float
        Potencia de la función.
    """
    T = sym.symbols('T')

    energia = lambda f: sym.integrate(abs(f)**2, (x, -sym.oo, sym.oo)) # Definición de energía en función de f

    potencia = lambda f: sym.limit((1/(2*T)*integrate(abs(f)**2, (x,-sym.oo,sym.oo))), T, sym.oo) # Definición de potencia en función de f

    # Evaluación de la energía y la potencia

    e = energia(fx).evalf()
    p = potencia(fx).evalf()

    return e, p

if __name__ == "__main__":
   
    from sympy.interactive import printing
    printing.init_printing(use_latex="mathjax")
    
    x, fx= funcion()
    
    display(fx)

    graficar(fx)

    energia, potencia = energia_potencia(x, fx)
    
    print("La energía de la función es:", energia)
    print("La potencia de la función es:", potencia)

    
