import numpy as np
import scipy
from scipy.fft import fft, ifft
from scipy.signal import fftconvolve
import soundfile as sf
import sounddevice as sd

def convolve(data1, data2):
    """
    Función para aplicar la convolución entre dos señales de audio.
    
    ------
    Parámetros:
    data1: array
        Array de la primera señal a convolucionar.
    
    data2: array
        Array de la segunda señal a convolucionar. 
    
    ------
    Returns:

    convolucion: array
        Array de las señales convolucionadas.
    """

    muestras1 = data1.shape[0]
    muestras2 = data2.shape[0]

    if muestras1 > 500 & muestras2 > 500:
        convolucion = scipy.signal.fftconvolve(data1,data2, "same")
    else:
        convolucion = np.convolve(data1, data2, "same")
        
    
    return convolucion

if __name__ == "__main__":
    from ejercicio_3 import cargar

    data1, fs1 = cargar("Sine_Sweep.wav")
    data2, fs2 = cargar("Filtro_Inverso.wav")

    convolucion = convolve(data1, data2)

    