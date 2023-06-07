import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

def convolucion(audioData_1, audioData_2):
    """
    Aplica la convolución entre dos señales de audio utilizando la librería numpy.

    Args:
        audioData_1 (array-like): Valores de amplitud de la señal 1.
        audioData_2 (array-like): Valores de amplitud de la señal 2.

    Returns:
        audioData_convol (ndarray): Valores de amplitud de la señal resultante de la convolución.

    La función realiza la convolución entre las señales `audioData_1` y `audioData_2`.
    Si la cantidad de muestras de ambas señales es mayor a 500, se realiza la convolución completa utilizando el modo 'full'.
    En caso contrario, se realiza la convolución con longitud de la señal más larga utilizando el modo 'same'.
    """
    if len(audioData_1) > 500 and len(audioData_2) > 500:
        audioData_convol = np.convolve(audioData_1, audioData_2, mode='full')
    else:
        audioData_convol = np.convolve(audioData_1, audioData_2, mode='same')

    return audioData_convol

if __name__ == "__main__":
    # Cargar los archivos de audio
    audioData_1, fs_1 = sf.read('impulso.wav')
    audioData_2, fs_2 = sf.read('ruido_rosa.wav')

    # Realizar la convolución
    resultado_convolucion = convolucion(audioData_1, audioData_2)
    
    # Graficar el resultado de la convolución
    plt.plot(resultado_convolucion)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Convolución entre audioData_1 y audioData_2')
    plt.show()

