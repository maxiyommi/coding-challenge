import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

f = sp.Piecewise(
    (0, x <= 0),
    (x, (x > 0) & (x <= 1)),
    (2 - x, (x > 1) & (x < 2)),
    (0, x >= 2)
)

p = sp.plot(f, (x, -1, 3), show=False, line_color='blue', title='Piecewise Function $f(x)$')
p.show()

totalEnergy = sp.integrate(f**2, (x, 0, 2))

print("La enería total de la señal: ", totalEnergy)
print("Dado que la señal tiene energía total finita, su potencia promedio es nula")