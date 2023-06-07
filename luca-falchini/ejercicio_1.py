import sympy as sym
from sympy.plotting import plot
from sympy import exp, Heaviside
from sympy import limit, integrate # función limite y integral

# 1- Expresar la función de manera simbólica.
x = sym.Symbol('x')
f1 = 0
f2 = x
f3 = 2-x
f4 = 0
f = sym.Piecewise((f1, x<=0),(f2, (x>0)&(x<=1)),(f3, (x>1)&(x<2)),(f4, x>=2))   # Defino la función a trozos

T = sym.Symbol('T')
E =  integrate(abs(f)**2,(x,-sym.oo, sym.oo))   # Energía de la señal
P = limit((1/(2*T)*integrate(abs(f)**2,(x,-sym.oo, sym.oo))),T,sym.oo)  # Potencia de la señal

if __name__ == "__main__":
    # 2- Graficar la expresión simbólica.
    plot(f, title="Función a trozos")
    # 3- Calcular (si existe) el valor numérico de la energía total y potencia promedio de la función.
    print(E.evalf())
    print(P.evalf())