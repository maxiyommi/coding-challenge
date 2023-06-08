import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

def lectura(archivo):
    """
    Esta función lee un archivo de audio y devuelve los datos del audio y la frecuencia de muestreo.
    ---
    Parametros:
        archivo: archivo.wav
            La ruta del archivo de audio.

    Devuelve:
        data: array
            Los datos del audio.
        fs: int
            La frecuencia de muestreo del audio.
    """
    data, fs = sf.read(archivo)
    return data, fs

def ej3(data, fs):
    """
    Esta función calcula el valor máximo, el valor mínimo y el promedio de la metadata de un archivo.
    ---
    Parametros:
        data: array
            La serie de datos.
        fs: int
            La frecuencia de muestreo de los datos.

    Devuelve:
        maximo: float
            El valor máximo de la serie de datos.
        minimo: float
            El valor mínimo de la serie de datos.
        promedio: float
            El promedio de la serie de datos.
    """

    maximo = max(data)
    minimo = min(data)
    promedio = sum(data)/len(data)

    return maximo, minimo, promedio

def grafico_3(data, fs, promedio):
    """
    Esta función grafica una señal de audio junto con una línea que representa su promedio.
    ---
    Parametros:
        data: array
            La serie de datos del archivo de audio.
        fs: int
            La frecuencia de muestreo de los datos.
        promedio: float
            El promedio de la serie de datos.
    """
    n = np.linspace(0, len(data) / fs, len(data))
    prom = np.ones(len(data)) * promedio
    plt.plot(n, data, label='Señal')
    plt.plot(n, prom, 'r', label='Promedio')
    plt.title('Señal de audio y su promedio')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.legend()

    plt.show()
