import wavio
import numpy as np
import matplotlib.pyplot as plt

def ValoresWav(señal):

    """
    Calcula los valores máximos, mínimos, promedio y duración de una señal de audio en formato .wav.

        Parámetros:
             señal (str): Nombre del archivo de audio en formato .wav.

        Retorno:
            tupla: (valor_max, valor_min, valor_promedio, duracion, señal)
                - valor_max: Valor máximo de la señal.
                - valor_min: Valor mínimo de la señal.
                - valor_promedio: Valor promedio de la señal.
                - duracion: Duración del audio en segundos.
                - señal: Señal de audio original como array de NumPy.
    """

    # 1. Cargar el archivo de audio y leer su metadata
    wav = wavio.read(señal)

    # Obtener la señal de audio y la tasa de muestreo
    y = wav.data.flatten()  # Aplanar la señal si es estéreo
    sr = wav.rate

    # Obtener la duración del audio
    duracion = len(y) / sr

    # 2. Obtener los valores máximos y mínimos
    valor_max = np.max(y)
    valor_min = np.min(y)

    # 3. Obtener el valor promedio de la señal
    valor_promedio = np.mean(y)

    return valor_max,valor_min,valor_promedio,duracion, y

def plotValWav(valor_max,valor_min,valor_promedio,duracion,y):
    """
    Generates a visualization of an audio signal along with its maximum, minimum, and average values.

    Parameters:
    - valor_max (float): The maximum value of the audio signal.
    - valor_min (float): The minimum value of the audio signal.
    - valor_promedio (float): The average value of the audio signal.
    - duracion (float): The duration of the audio signal in seconds.
    - y (numpy.ndarray): The NumPy array containing the audio signal data.

    Returns:
    - None: The function does not return any value.

    Generates a visual representation of the audio signal 'y' using Matplotlib. It overlays 
    horizontal lines at the positions of the maximum, minimum, and average values to highlight 
    these characteristics. The plot is titled, labeled, and includes a legend.

    """
    # Crear la gráfica
    tiempo = np.linspace(0, duracion, len(y))
    plt.figure(figsize=(14, 6))
    plt.plot(tiempo, y, label='Señal de audio')
    plt.axhline(y=valor_max, color='r', linestyle='--', label=f'Máximo')
    plt.axhline(y=valor_min, color='b', linestyle='--', label=f'Mínimo')
    plt.axhline(y=valor_promedio, color='g', linestyle='-', label=f'Promedio')

    # Añadir títulos y leyenda
    plt.title('Señal de Audio con Máximos, Mínimos y Promedio')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__=="__main__":

    valor_max,valor_min,valor_promedio,duracion,y = ValoresWav("Challenge/IR1.wav")

    # Mostrar metadata
    print(f'Duración del audio: {duracion} segundos')
    print(f'Valor máximo: {valor_max}')
    print(f'Valor mínimo: {valor_min}')
    print(f'Valor promedio: {valor_promedio}')

    plotValWav(valor_max,valor_min,valor_promedio,duracion,y)