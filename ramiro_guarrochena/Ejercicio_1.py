import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def f(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    elif 1 < x < 2:
        return 2 - x
    else:
        return 0

x_values = np.linspace(-1, 3, 400)
y_values = np.array([f(x) for x in x_values])
plt.plot(x_values, y_values, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

x = sp.symbols('x')

f = sp.Piecewise(
    (0, x <= 0),
    (x, (x > 0) & (x <= 1)),
    (2 - x, (x > 1) & (x < 2)),
    (0, x >= 2)
)

energy_expr = sp.integrate(sp.Abs(f)**2, (x, -sp.oo, sp.oo))

sp.pprint(energy_expr)

energy_value = energy_expr.evalf()

print(f"Energía total de la señal: {energy_value}")



