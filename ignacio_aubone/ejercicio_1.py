import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

def funcion_1():
    """
    Brinda información sobre la función dada en el ejercicio_1 del Coding Challenge.
    
    Nota
    ----
    No tiene parámetros de entrada ni returns.
    Al llamarla, realiaza lo siguiente:
        - Imprime la función partida simbólicamente.
        - Genera un gráfico de la función (convertida en una función de numpy).
        - Imprime los valores de energía total y potencia promedio de la función.
    
    """
    # Expresar la función partida de manera simbólica
    x = sp.symbols('x')
    f0 = 0
    f1 = x
    f2 = 2 - x
    f = sp.Piecewise((f0,(x<0)), (f1,(0<=x)&(x<1)), (f2,(1<=x)&(x<2)), (f0,(x>=2)))

    # Imprimir la función simbólica
    print("f(x) =", f)
    print('-'*25)

    # Conversión de la función simbólica a una función numpy
    f_np = sp.lambdify(x, f)
    x_val = np.linspace(-3, 5, 1000)
    y_val = f_np(x_val)

    # Graficar la expresión simbólica
    fig, ax = plt.subplots()
    ax.plot(x_val, y_val, color='blue', linewidth=2)
    ax.set_xlim(-3, 5)
    ax.set_ylim(-1, 2)
    ax.set_xlabel('x', fontsize=20)
    ax.set_ylabel('f(x)', fontsize=20)
    plt.show()

    # Cálculo de la Energía total
    L = sp.symbols('x')
    energia = sp.integrate(f**2, (L, -sp.oo, sp.oo))
    print('Energía promedio:', energia)
    print('-'*25)

    # Cálculo de la potencia promedio
    if math.isinf(energia):
        potencia = sp.limit((1/(2*L)), L, sp.oo) * energia
        print('Potencia promedio: ', potencia)
    else:
        print('Como la energía total es una constante, la potencia promedio es cero y la señal es de energía')
        
funcion_1()

