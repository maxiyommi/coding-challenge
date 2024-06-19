import numpy as np
import matplotlib.pyplot as plt

def secuencia_aleatoria(num_elementos, min_valor, max_valor, seed=None):
    """
    Genera una secuencia aleatoria de números.

    Parámetros:
    - num_elementos (int): Número de elementos en la secuencia.
    - min_valor (float): Valor mínimo para los números generados.
    - max_valor (float): Valor máximo para los números generados.
    - seed (int or None): Semilla para la generación de números aleatorios.

    Retorna:
    - secuencia (numpy.ndarray): Secuencia aleatoria generada.
    """
    if seed is not None:
        np.random.seed(seed)
    secuencia = np.random.uniform(min_valor, max_valor, num_elementos)
    return secuencia

def maximo_y_minimo(secuencia):
    """
    Encuentra los índices correspondientes al máximo y mínimo valor en una secuencia.

    Parámetros:
    - secuencia (numpy.ndarray): Secuencia de números.

    Retorna:
    - indice_maximo (int): Índice del valor máximo en la secuencia.
    - indice_minimo (int): Índice del valor mínimo en la secuencia.
    """
    indice_maximo = np.argmax(secuencia)
    indice_minimo = np.argmin(secuencia)
    return indice_maximo, indice_minimo

def graficar_secuencia_aleatoria(secuencia, maximo, minimo):
    """
    Grafica una secuencia aleatoria junto con sus valores máximo y mínimo.

    Parámetros:
    - secuencia (numpy.ndarray): Secuencia de números.
    - maximo (int): Índice del valor máximo en la secuencia.
    - minimo (int): Índice del valor mínimo en la secuencia.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(secuencia, label='Secuencia aleatoria')
    plt.scatter(maximo, secuencia[maximo], label=f'maximo ({secuencia[maximo]:.2f})')
    plt.scatter(minimo, secuencia[minimo], label=f'minimo ({secuencia[minimo]:.2f})')
    plt.title('Secuencia Aleatoria')
    plt.xlabel('Indice')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()

num_elementos = 30
min_valor = 0
max_valor = 10
secuencia = secuencia_aleatoria(num_elementos, min_valor, max_valor, seed=0)

maximo, minimo = maximo_y_minimo(secuencia)

graficar_secuencia_aleatoria(secuencia, maximo, minimo)
