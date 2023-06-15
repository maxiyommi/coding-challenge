import matplotlib.pyplot as plt

def graficar_func(x_vals, f_vals):
    """
   Realiza el gráfico de una función.

    Parámetros
    ----------
    x_vals : array.
        Array con mil puntos equidistantes entre el intervalo [-5, 5].
    f_vals : array.
        Array que contiene los valores de la función al evaluarla en los valores x_val.
    

    Returns
    -------
    Gráfico de la función.

    """
    plt.plot(x_vals, f_vals, color='red', label='Señal')
    plt.title('Señal')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(int(min(x_vals)), int(max(x_vals))+1))  # Establece los ticks del eje x con saltos de a uno
    plt.tight_layout()  # Añade un espaciado automático para centrar el gráfico
    plt.show()
    return

