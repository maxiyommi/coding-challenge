# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:50:46 2023

@author: Usuario
"""
import numpy as np
from scipy.signal import fftconvolve

def convolucion_señales(audioData_1, audioData_2):
    """
    Realiza la convolución entre dos señales de audio

    Parámetros
    ----------
    audioData_1 : Array
        Valores de amplitud de la señal 1.
    audioData_2 : Array
        Valores de amplitud de la señal 2.

    Returns
    -------
    audioData_convol : Array
        Valores de amplitud de la señal resultante de la convolución.

    """
    # Verificar la cantidad de muestras de cada señal
    n_muestras1 = len(audioData_1)
    n_muestras2 = len(audioData_2)

    if n_muestras1 <= 500 and n_muestras2 <= 500:
        # Usar numpy.convolve para la convolución
        audioData_convol = np.convolve(audioData_1, audioData_2, mode='full')
    else:
        # Usar scipy.signal.fftconvolve para la convolución
        audioData_convol = fftconvolve(audioData_1, audioData_2, mode='full')

    return audioData_convol

if __name__ == '__main__':
    from Ejercicio_3 import lectura_wav
    data1, fs1 = lectura_wav('sine_sweep.wav')
    data2, fs2 = lectura_wav('impulso.wav')
    convolucion_señales(data1, data2)
