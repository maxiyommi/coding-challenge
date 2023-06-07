import numpy as np
import scipy
from scipy.signal import fftconvolve
import soundfile as sf
import matplotlib.pyplot as plt

def ej4(audioData_1,audioData_2):
    """
    Esta función realiza la convolución de dos señales de audio.
    En caso de que los archivos tengan mas de 500 muestras se utiliza la libreria Scipy, y en caso de que tengan menos de 500 muestras se utiliza la libreria Numpy.
    ---
    Parametros:
        audioData_1: array
            La data de la primera señal de audio.
        audioData_2: array
            La data de segunda señal de audio.

    Devuelve:
        audioData_convol: array
            El resultado de la convolución de las dos señales de audio.
    """
    if len(audioData_1)>500:
        audioData_convol = fftconvolve(audioData_1,audioData_2,'same')
    else:
        audioData_convol = np.convolve(audioData_1,audioData_2)
    return audioData_convol

