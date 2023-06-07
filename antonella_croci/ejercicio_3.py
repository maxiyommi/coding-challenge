import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

def cargar(archivo):
    """
    Función que carga un archivo de audio para extraer información que caracteriza su contenido.

    ------
    Parámetros:

    archivo: archivo .wav
        Directorio del archivo .wav a cargar para extraer su información.
    
    ------
    Returns:
    
    data: array
        Array representativo de la señal de audio.
    
    fs: int
        Frecuencia de muestreo extraida de la señal de audio.
    """

    data, fs = sf.read(archivo)

    return data, fs

def max_min_audio(data):
    """
    Función que obtiene los valores máximos y mínimos del archivo de audio.

    ------
    Parámetros:

    data: array
        Array extraido de la señal de audio.
    
    ------
    Returns:
    
    maximo: float
        Valor de amplitud máxima de la señal de audio.
    
    minimo: float
        Valor de amplitud mínima de la señal de audio.
    """

    maximo = np.max(data)
    minimo = np.min(data)

    return maximo, minimo

def mean(data):
    """
    Calcula el valor promedio de la señal de audio.

    ------
    Parámetros:

    data: array
        Array extraido de la señal de audio. 
    
    ------
    Returns:

    promedio: float
        Valor promedio de la señal de audio.
    """

    promedio = np.mean(data)

    return promedio

def grafico3(data, fs, promedio):
    """
    Grafica el archivo de audio junto con su promedio.

    ------
    Parámetros:

    data: array
        Array extraído de la señal de audio. 
    
    fs: int
        Frecuencia de muestreo extraída de la señal de audio.
    
    Promedio: float
        Valor promedio de la señal de audio.
    
    ------
    Returns: matplotlib plot
        Gráfico de la señal junto con su promedio.
    """
     
    t = np.linspace(0., data.shape[0]/fs, data.shape[0]) # Definición de la duración de la señal.
    promedio = np.ones(len(data)) * promedio # Array generado para que coincida la forma del promedio con la del audio y sea posible graficar.
    
    plt.plot(t, data, "pink", label="Audio")
    plt.plot(t, promedio, "purple", label="Valor promedio")
    plt.legend(loc="upper right")
    plt.title("Audio y valor promedio.")
    plt.xlabel("Tiempo $[s]$")
    plt.ylabel("Amplitud")
    plt.show()


if __name__ == "__main__":
    data, fs = cargar('IR1.wav')

    max, min = max_min_audio(data)
    
    print("El valor máximo del audio es:", max)
    print("El valor mínimo del audio es:", min)

    promedio = mean(data)
    print("El promedio de la señal de audio es:", promedio)
    
    grafico3(data, fs, promedio)