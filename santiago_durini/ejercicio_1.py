import sympy
from sympy import limit, integrate


def ej1():
    """
    Esta función genera la función f(x) utilizando SymPy y la grafica en un rango dado.
    ---
    Devuelve:
        f: La función f(x) definida utilizando SymPy.
    """
    x = sympy.symbols('x')
    f = sympy.Piecewise((0, x <= 0), (x, (x > 0) & (x < 1)), (2 - x, (x > 1) & (x < 2)), (0, x >= 2))

    sympy.plot(f, (x, -1, 3), xlabel='x', ylabel='f(x)', title='Grafico de f(x)')
    return f

def EyP(funcion):
    """
    Esta función calcula la energía y la potencia promedio de una función dada.
    ---
    Parametros:
        funcion: La función para la cual se desea calcular la energía y la potencia.

    Devuelve:
        Energia_resultado: float
            La energía de la función. Se utilizó un intervalo de integracion acotado para que Python lea el valor.
        Potencia: float
            La potencia promedio de la función.
    """

    x,T = sympy.symbols('x T')
    Energia = integrate(abs(funcion)**2,(x,-sympy.oo, sympy.oo))
    Energia_resultado =  integrate(abs(funcion)**2,(x,-2, 4))
    Potencia = limit(1/(2*T)*Energia,T,sympy.oo)

    return Energia_resultado, Potencia
