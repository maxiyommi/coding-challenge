from sympy import symbols, Piecewise, integrate, oo, limit, pprint
from sympy.plotting import plot


def funcion_a_trozos(x):
    """
    La función genera una función a trozos ya definida por la consigna pedida en el enunciado del ejercicio n˚1.
    Parámetros:
        x: La función recibe una variable previamente inicializada con el método symbols de sympy, que será la variable de la función.
    Returns:
        funcion: se devuelve la función de tipo Piecewise.
    """
    f1 = 0
    f2 = x
    f3 = 2 - x
    f4 = 0

    condiciones = [
        (f1, x <= 0),
        (f2, (x > 0) & (x <= 1)),
        (f3, (x > 1) & (x < 2)),
        (f4, x >= 2),
    ]

    funcion = Piecewise(*condiciones)

    return funcion


def grafico_funcion(funcion):
    """
    La función se encarga de graficar la funcion recibida por parámetro.
    Parámetros:
        funcion: se recibe como parametro la función de tipo Piecewise.
    Returns:
        -
    """
    plot(funcion)


def energia_señal(funcion, variable_integrar):
    """
    La función se encarga de calcular la energía de la señal determinada por la función recibida por parámetro y su variable a integrar.
    Parámetros:
        funcion: función de tipo Piecewise.
        variable_integrar: variable inicializada con el método symbols de sympy.
    Returns:
        energia: se retorna el valor de la energía, de tipo float.
    """
    energia = integrate(abs(funcion) ** 2, (variable_integrar, -oo, oo)).doit()
    return energia


def potencia_señal(funcion, variable_integrar, variable_limite):
    """
    La función se encarga de calcular la potencia de la señal determinada por la función recibida por parámetro, su variable a integrar y la variable con la que se tomará el límite.
    Parámetros:
        funcion: función de tipo Piecewise.
        variable_integrar: variable inicializada con el método symbols de sympy.
        variable_limite: variable inicializada con el método symbols de sympy.
    Returns:
        energia: se retorna el valor de la potencia, de tipo float.
    """
    potencia = limit(
        (
            1
            / (2 * variable_limite)
            * (integrate(abs(funcion) ** 2, (variable_integrar, -oo, oo)).doit())
        ),
        variable_limite,
        oo,
    )
    return potencia


if __name__ == "__main__":
    x, T = symbols("x T")

    funcion = funcion_a_trozos(x)
    grafico_funcion(funcion)
    energia = energia_señal(funcion, x)
    potencia = potencia_señal(funcion, x, T)
    print("La señal está caracterizada por: ")
    pprint(funcion)
    print(
        f"\nLa misma tiene una energía de valor {energia}\nY una potencia igual a {potencia}"
    )
