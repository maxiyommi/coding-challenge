import numpy as np
import matplotlib.pyplot as plt

def Numeros(AmplitudIn,AmplitudFin,Cantidad):

    """
    Genera una secuencia aleatoria de números uniformes con la cantidad especificada y devuelve la secuencia, 
    el índice del valor máximo y el índice del valor mínimo en la secuencia.

    Parámetros:
        AmplitudIn (float): Límite inferior del rango uniforme para generar los números aleatorios.
        AmplitudFin (float): Límite superior del rango uniforme para generar los números aleatorios.
        Cantidad (int): Cantidad de números aleatorios a generar.

    Retorno:
        tupla: (secuencia, indice_max, indice_min)
            - secuencia: Array de NumPy que contiene la secuencia de números aleatorios generados.
            - indice_max: Índice del valor máximo dentro de la secuencia.
            - indice_min: Índice del valor mínimo dentro de la secuencia.
    """

    secuencia = np.random.uniform(AmplitudIn, AmplitudFin, Cantidad)

    # 2. Encontrar los índices correspondientes a los valores máximos y mínimos de la secuencia
    indice_max = np.argmax(secuencia)
    indice_min = np.argmin(secuencia)

    return secuencia, indice_max, indice_min

def plot_Num(secuencia,indice_max,indice_min):

    """
    Generates a visualization of a random sequence along with its maximum and minimum values and their corresponding indices.

    Parameters:
    - secuencia (numpy.ndarray): The NumPy array containing the random sequence values.
    - indice_max (int): The index of the maximum value in the sequence.
    - indice_min (int): The index of the minimum value in the sequence.

    Returns:
    - None: The function does not return any value.

    Creates a visual representation of the random sequence 'secuencia' using Matplotlib. It overlays 
    markers at the positions of the maximum and minimum values to highlight these points and 
    includes their corresponding indices. The plot is titled, labeled, and includes a legend.

    """
    # 3. Graficar la secuencia con los máximos y mínimos en un mismo gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(secuencia, marker='o', label='Secuencia')
    plt.plot(indice_max, secuencia[indice_max], 'ro', label='Máximo')
    plt.plot(indice_min, secuencia[indice_min], 'go', label='Mínimo')

    # Añadir títulos y leyenda
    plt.title('Secuencia Aleatoria con Máximos y Mínimos')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__=="__main__":

    secuencia, indice_max, indice_min= Numeros(0,10,30)

    plot_Num(secuencia,indice_max,indice_min)