'''
Ejercicio_1
Dada la siguiente función continua:

![](ejercicio_1.png)
<!---
$$ f(x)=\begin{cases} 
0, \text{ para } x<=0 \\  
x, \text{  para } 0<x<=1 \\
2-(x), \text{ para } 1<x<2 \\ 
0, \text{ para } x>=2 \\  
\end{cases}$$
-->

1. Expresar la función de manera simbólica.
2. Graficar la expresión simbólica.
3. Calcular (si existe) el valor numérico de la energía total y potencia promedio de la función.
'''

import matplotlib.pyplot as plt
import numpy as np

# 1 y 2

def funcion(x):

    """
    Compute the value of a piecewise function.

    Parameters:
    x (float): The input value for the function.

    Returns:
    float: The output value of the function based on the input.

    Description:
    This function evaluates a piecewise function defined as follows:
    - If x <= 0: return 0
    - If 0 < x <= 1: return x
    - If 1 < x <= 2: return 2 - x
    - If x > 2: return 0
    """

    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    elif 1 < x <= 2:
        return 2 - x
    else:
        return 0

# Rango de X en relacion a Y
rangoX = np.linspace(-2, 4, 1000)
valoresY = [funcion(x) for x in rangoX]

# Grafico
plt.figure(figsize = (5, 2))
plt.plot(rangoX, valoresY,)
plt.title('Función Por Partes')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth = 1)
plt.axvline(0, color='black', linewidth = 1)
plt.grid(True)
plt.legend()
plt.show()

# 3

def calculoEnergía(funcion, rango):
    
    """
    Calculate the energy of the function over a given range.

    Parameters:
    funcion (function): The function for which the energy is to be calculated.
    rango (iterable): The range of x values over which to calculate the energy.

    Returns:
    float: The energy of the function over the specified range.

    Description:
    This function computes the energy of the given function over the specified range.
    The energy is calculated as the sum of the squared absolute values of the function
    evaluated at each point in the range.
    """

    valoresY = [funcion(x) for x in rango]

    return np.sum(np.abs(valoresY)**2)

def calculoPotencia(funcion, rango):
    
    """
    Calculate the power of the function over a given range.

    Parameters:
    funcion (function): The function for which the power is to be calculated.
    rango (iterable): The range of x values over which to calculate the power.

    Returns:
    float: The power of the function over the specified range.

    Description:
    This function computes the power of the given function over the specified range.
    The power is calculated as the mean of the squared absolute values of the function
    evaluated at each point in the range.
    """

    valoresY = [funcion(x) for x in rango]

    return np.mean(np.abs(valoresY)**2)

energia = calculoEnergía(funcion, rangoX)
potencia = calculoPotencia(funcion, rangoX)

print("Energía de la función:", energia)
print("Potencia de la función:", potencia)

