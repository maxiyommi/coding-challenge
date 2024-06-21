import sympy as sp
from sympy.plotting import plot
from sympy import integrate, limit
import numpy as np
import matplotlib.pyplot as plt

t= sp.symbols('t')
T = sp.symbols('T')
t1 = 0
t2 = 1
t3 = 2
f1 = (0, t <= t1)
f2 = (t, (t1 < t)&(t<= t2) )
f3 = (2-t, (t1 < t)&(t< t3))
f4 = (0, t >= t3)
f_trozos = sp.Piecewise(f1,f2,f3,f4)


def calculo_energia_potencia(funcion):
    """
  Calculates the energy and power of a piecewise function defined symbolically.

  This function takes a piecewise function `funcion` defined using the `sympy.Piecewise`
  constructor and calculates its energy and power. The function is assumed to be defined
  over time (represented by the symbolic variable `t`).

  Args:
      funcion (sympy.Piecewise): The piecewise function for which to calculate energy and power.

  Returns:
      None: The function prints the calculated energy and power to the console.

  Raises:
      ValueError: If the integration of the absolute value of the function squared does not converge.

  Notes:
      - The function assumes the piecewise function is defined for all real numbers
        (-∞, ∞). If the function has a finite domain, the integration limits in the
        `integrate` calls should be adjusted accordingly.
      - The power calculation assumes the function has a finite period `T`. If the
        function is aperiodic, the power calculation will not be meaningful.
"""
    energia = float(integrate(abs(funcion)**2,(t, -sp.oo, sp.oo)))
    if energia != 0:
        print('La energia de la funcion es',energia,' y la potencia es 0.')
    else:
        potencia = float(limit(1/(2*T)*integrate(abs(funcion)**2,(t, -sp.oo, sp.oo)), T, sp.oo))
        print('La energia de la funcion es infinita y la potencia es ',potencia,'.')
 
    

if __name__ == '__main__':
    calculo_energia_potencia(f_trozos)


    



