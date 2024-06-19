import matplotlib.pyplot as plt
import sympy as sp
import numpy as np


def Energia_Potencia(f,x):
    
    """
    Calcula la energía total y la potencia promedio de una señal representada por una función simbólica.

    Parámetros:
        - f (sympy.Expr): La función simbólica f(x) que representa la señal.
        - x (sympy.Symbol): La variable simbólica de integración.

    Retorno:
        - tuple: (E, P)
        - E (sympy.Expr): La energía total de la señal (valor simbólico).
        - P (sympy.Expr): La potencia promedio de la señal (valor simbólico)."""
    
    T = sp.symbols('T')

    # Calcular 
    E = sp.integrate(f**2, (x, -sp.oo, sp.oo))
    P = sp.limit((1/(2*T)*sp.integrate(f**2,(x,-sp.oo, sp.oo))),T,sp.oo)
    
    return E,P

def funcion():

    """
    Defines a piecewise function f(x) and generates its corresponding graph.

    Returns:
    - f (sympy.Expr): The symbolic representation of the piecewise function f(x).
    - x (sympy.Symbol): The symbolic variable used in the definition of the function.

    Generates a graph of the piecewise function f(x) defined as:
        - 0 if x <= 0
        - x if 0 < x <= 1
        - 2 - x if 1 < x <= 2
        - 0 if x > 2

    The function creates a symbolic representation of the function using SymPy, converts it 
    to a NumPy-compatible function, evaluates it for a range of x values, and generates 
    a labeled plot using Matplotlib.

    """

    # Definir la variable simbólica
    x = sp.Symbol('x')

    # Definir la función por partes
    f = sp.Piecewise(
        (0, x <= 0),
        (x, (x > 0) & (x <= 1)),
        (2 - x, (x > 1) & (x <= 2)),
        (0, x > 2))

    # Convertir la función simbólica a una función lambda para evaluación numérica
    f_lambda = sp.lambdify(x, f, 'numpy')

    # Definir el rango de x para la gráfica
    x_vals = np.linspace(-1, 3, 400)
    y_vals = f_lambda(x_vals)

    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='f(x)')

    # Añadir títulos y leyenda
    plt.title('Gráfica de la función por partes')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

    return f,x

if __name__=="__main__":

    f,x = funcion()

    E,P = Energia_Potencia(f,x)

    # Mostrar los resultados
    print(f'Energía total: {E.evalf()}')
    print(f'Potencia promedio: {P.evalf()}')