import sympy as sp
import numpy as np

def eyp_señal(L1, L2, L3):
    """
   Genera una función partida recibiendo como entrada los valores límite de las particiones de la misma.
   Además calcula la energía y la potencia media de la señal.
   Por último, genera dos arrays para trazar la función.

    Parámetros
    ----------
    L1 : float.
        Límite inferior de la partición.
    L2 : float.
        Límite intermedio de la partición.
    L3 : Float.
        Límite superior de la partición.


    Returns
    -------
    x_vals : array.
        Array con mil puntos equidistantes entre el intervalo [-5, 5].
    f_vals : array.
        Array que contiene los valores de la función al evaluarla en los valores x_val.

    """
    x, T = sp.symbols('x T')
    f = sp.Piecewise(
    (0, x <= L1),
    (x, sp.And(L1 < x, x <= L2)),
    (2 - x, sp.And(L2 < x, x < L3)),
    (0, x >= L3)
)

    # Función lambda para trazar f
    f_lambda = sp.lambdify(x, f, modules=['numpy'])

    # Cálculo de energía
    E = sp.integrate(f**2, (x, -sp.oo, sp.oo))

    # Cálculo de potencia
    P = sp.limit((1/(2*T) * sp.integrate(f**2, (x, -sp.oo, sp.oo))), T, sp.oo)

    # Trazar la función
    x_vals = np.linspace(-5, 5, 1000) #crea un arreglo de 1000 puntos equidistantes en el intervalo [-5, 5]. 
    f_vals = f_lambda(x_vals) #evalúa la función f en los puntos definidos por x_vals.
    

    print('La energía de la señal es:', E)
    print('La potencia de la señal es:', P)
    
    return x_vals, f_vals

if __name__ == "__main__":
    from graficar_func import graficar_func
    x, f=eyp_señal(0,1,2)
    graficar_func(x, f)