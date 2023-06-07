import sympy as sym

def calcular_caracteristicas_funcion():
    """
    Calcula y grafica las características de una función utilizando la biblioteca sympy y matplotlib.

    La función realiza los siguientes pasos:
    1. Define una función 'f' y la expresa de forma simbolica utilizando la biblioteca `sympy`.
    Esta función tiene diferentes valores dependiendo de la variable 'x'.
    2. Grafica la expresion simbolica de la funcion 'f'.
    3. Calcula la energía total de la función `f` integrando el valor absoluto de `f` al cuadrado desde menos infinito hasta infinito.
    4. Calcula la potencia promedio de la función `f` tomando el límite de la integral del valor absoluto de `f` al cuadrado dividido por el doble de `T`, cuando `T` tiende a infinito.
    5. Imprime en la consola el valor de la energía total y la potencia promedio de la función.

    No tiene argumentos de entrada ni salida. Los resultados se imprimen directamente en la consola.
    """
    x, T = sym.symbols('x T')
    f = sym.Piecewise((0, x <= 0), (x, (0 < x) & (x <= 1)), (2 - x, (1 < x) & (x < 2)), (0, x >= 2))

    # Calcular la energía total y potencia promedio
    Energia = sym.integrate(abs(f)**2, (x, -sym.oo, sym.oo)).doit()
    Potencia = sym.limit((1 / (2 * T) * sym.integrate(sym.Abs(f)**2, (x, -sym.oo, sym.oo))), T, sym.oo)

    # Graficar la función
    sym.plot(f, (x, -2, 3), title='Gráfica de f(x)')    
    print("Energía total:", Energia)
    print("Potencia promedio:", Potencia)

if __name__ == "__main__":
    calcular_caracteristicas_funcion()
