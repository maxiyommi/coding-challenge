import numpy as np


def secuencia(Amplitud, Elementos):
    """
   Genera una secuencia aleatoria de n elementos y de cierta amplitud, ambos parámetros elegidos por el usuario.

    Parámetros
    ----------
    Amplitud: int
        Amplitud máxima de la secuencia aleatoria.
    Elementos: int
        Cantidad de elementos de la secuencia aleatoria.    
        
    Returns
    -------
    s : array.
        Array con los valores de la secuencia aleatoria.
    maximo : float.
        Flotante con información sobre el valor máximo.
    minimo : float.
        Flotante con información sobre el valor mínimo.
    indice_maximo: int.
        Entero con información sobre el indice del array correspondiente al máximo.
    indice_minimo: int.
        Entero con información sobre el indice del array correspondiente al máximo.

    """
    # Generar una secuencia aleatoria de números entre 0 y 10
    s = Amplitud * np.random.rand(Elementos)

    # Encontrar los máximos y mínimos de la secuencia
    maximo = np.max(s)
    minimo = np.min(s)
    indice_maximo = np.argmax(s)
    indice_minimo = np.argmin(s)

    # Imprimir los índices del valor máximo y mínimo
    print('Índice del valor máximo:', indice_maximo)
    print('Índice del valor mínimo:', indice_minimo)
    
    return s, maximo, minimo, indice_maximo, indice_minimo





if __name__ == "__main__":
    from graficar_sec import graficar_sec
    secuencia, m, mi, ima, imi = secuencia(10,30)
    graficar_sec(secuencia, m, mi, ima, imi)

