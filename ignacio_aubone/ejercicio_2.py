import numpy as np
import matplotlib.pyplot as plt

def funcion_2():
    """
    Brinda información sobre una secuencia particular.
    
    Nota
    ----
    No tiene parámetros de entrada ni returns.
    Al llamarla, realiza lo siguiente:
        - Genera una secuencia aleatoria de 30 elementos, con amplitud entre 0 y 10.
        - Imprime los índices en los que se encuentran los valores máximo y mínimo de la secuencia.
        - Genera un gráfico de la secuencia resaltando el valor máximo y el valor mínimo.
    
    """
    # Secuencia aleatoria de 30 elementos, con amplitud entre 0 y 10
    S = np.random.uniform(0, 10, 30)

    # Valores máximos y mínimos
    valor_maximo = max(S)
    valor_minimo = min(S)

    # Índices correspondientes a los valores máximos y mínimos
    indices_maximos = np.where(S == valor_maximo)[0]
    indices_minimos = np.where(S == valor_minimo)[0]
    print('El máximo se encuentra en el índice: ', indices_maximos)
    print('El mínimo se encuentra en el índice: ', indices_minimos)

    # Gráfico de la secuencia con los máximos y mínimos
    plt.stem(S, label='Secuencia aleatoria', basefmt='none')
    plt.stem(indices_maximos, S[indices_maximos], linefmt='r', basefmt='none', label='Valor máximo')
    plt.stem(indices_minimos, S[indices_minimos], linefmt='g', basefmt='none', label='Valor mínimo')
    plt.ylim(0, 13)
    plt.xlabel('Índice', fontsize=14)
    plt.ylabel('Amplitud', fontsize=14)
    plt.legend(fontsize=8)
    plt.show()

funcion_2()

