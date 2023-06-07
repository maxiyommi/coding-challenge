import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import limit, integrate
from sympy import symbols, Piecewise

# Ejercicio 1

# Definición de la función
def f(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    elif 1 < x < 2:
        return 2 - x
    else:
        return 0

# Generación de valores de x en el rango deseado
x_values = np.linspace(-1, 3, 1000)

# Evaluación de la función en los valores de x
y_values = [f(x) for x in x_values]

# Graficar la función
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de la función f(x)')
plt.grid(True)
plt.show()

t, T = sympy.symbols('t T')

# Para calcular la energía total es necesario definir simbólicamente la función f para poder utilizarla en E =  integrate(abs(f)**2,(t,-sympy.oo, sympy.oo))
x = symbols('x')
f = Piecewise((0, x <= 0), (x, (0 < x) & (x <= 1)), (2 - x, (1 < x) & (x < 2)), (0, x >= 2))
# Para la Energía Total:
energia_total_expr = abs(f)**2

# Utilizo la función evalf para evaluar expresión simbólica, sino el resulatdo arrojaba: Energía total: Integral(Abs(x)**2, (x, 0, 1)) + Integral(Abs(x - 2)**2, (x, 1, 2))
energia_total = integrate(energia_total_expr, (x, -sympy.oo, sympy.oo)).evalf()

print("Energía total:", energia_total)
# Para la Potencia Promedio:
P = limit((1/(2*T)*integrate(abs(f)**2,(x,-sympy.oo, sympy.oo))),T,sympy.oo)
print("Potencia promedio:", P)
# era de esperar que la Potencia Promedio sea 0 ya que la Energía Total