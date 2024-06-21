import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy import integrate
from sympy import symbols, Piecewise, And

def f(x):
    """
    Define una función por casos (piecewise) f(x) utilizando Sympy.

    Parámetros:
    x (símbolo): La variable independiente.
    jump (float, opcional): El valor del salto en x=2. Valor predeterminado es 0.

    Devuelve:
    sp.Expr: La expresión simbólica de la función por casos f(x).
    """
    x_sym = symbols('x')
    piecewise_f = Piecewise((0, x_sym <= 0),
                            (x_sym, And(0 < x_sym, x_sym <= 1)),
                            (2 - x_sym, And(1 < x_sym, x_sym < 2)),
                            (0, x_sym >= 2))
    return piecewise_f.subs(x_sym, x)

def plot_fx(f, x_range=(-1, 3), num_points=400):
    """
    Grafica la función f(x) en el rango especificado.

    Parámetros
    ----------
    f : función
        La función a graficar.
    x_range : tuple, opcional
        El rango de valores de x para graficar. Valor predeterminado es (-1, 3).
    num_points : int, opcional
        El número de puntos para graficar. Valor predeterminado es 400.

    Retorna
    -------
    None
    """
    ValoresX = np.linspace(x_range[0], x_range[1], num_points)
    ValoresY = np.array([f(x) for x in ValoresX])

    # Graficar la función
    plt.figure(figsize=(8, 6))
    plt.plot(ValoresX, ValoresY, label='$f(x)$')
    plt.title('Gráfico de $f(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.legend()
    plt.grid(True)
    plt.show()

def f_cuadrado(x):
    """
    Define una función que devuelve el cuadrado de f(x).

    Parámetros:
    x (float): El valor de entrada para la función.

    Devuelve:
    float: El cuadrado de f(x).
    """
    return f(x)**2

def calcular_potencia_infinito(f):
    """
    Calcula la potencia infinita de una función f(x).

    Parámetros
    ----------
    f : función
        La función para la οποία se calculará la potencia infinita.

    Retorna
    -------
    P : float
        La potencia infinita de la función f(x).

    Nota
    ----
    La potencia infinita se calcula como la integral de la función al cuadrado
    desde -infinito hasta infinito, dividida por 2 veces infinito.
    """
    x = sp.symbols('x')

    f_cuadrado = f(x)**2

    integral_infinito = sp.integrate(f_cuadrado, (x, -sp.oo, sp.oo))

    P = (1 / (2 * sp.oo)) * integral_infinito

    return P

plot_fx(f)

Energia, error = integrate.quad(f_cuadrado, 0, 2)
print (f"La energia total es: {Energia}")

potencia = calcular_potencia_infinito(f)
print(f"La potencia de la función f(x) es: {potencia}")
