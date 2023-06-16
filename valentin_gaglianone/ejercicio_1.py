import sympy as sym
x,f=sym.symbols("x f", real=True)
f=sym.Piecewise((0,(x<0)),(x,((0<=x) & (x<=1))),(2-x,((x>=1) & (x<2))),(0,(x>=2)))
print("la funcion definida por trozos es:")
sym.plot(f) 
print(f)
print("La energía de la señal es:")
Energia=sym.Integral(abs(f**2),(x, 0,2)) # tomamos limites de integracion 0 y 2 ya que fuera de ese rango la integral es igual a 0, asi ahorramos tiempo de computo.
a=Energia.evalf()
print(a)
print("Como la energía es finita, la potencia es 0")
