import matplotlib.pyplot as plt
import numpy as np


def grafico(data, fs=44100):
    """
    La función se encarga de graficar el dominio temporal de la señal de audio ingresada e imprimirla en la ventana interactiva correspondiente.
    ----------
    data : NumpyArray
        Array del audio a graficar.
    fs: Frecuencia de muestreo del audio a graficar.

    returns: None
    """
   
    fig, ax = plt.subplots(figsize=(20, 10))  # Crear una nueva figura
    timeValues = np.arange(0, len(data), 1) / fs
    ax.plot(timeValues, data)
    ax.set_title('convolución', size=16)
    ax.set_ylabel('amplitud')
    ax.set_xlabel("Tiempo (s)")
