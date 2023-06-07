# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:24:07 2023

@author: Franco
"""
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import fftconvolve


def cargar(file1,file2):
    """
    Función que realiza la carga de las dos señales que luego serán convolucionadas.
    Utiliza soundfile para leer los archivos de audio
    Parámetros:
    *data1, data2: metadatas de cada archivo
    *fs1, fs2: frecuencias de muestreo de cada archivo de audio
    
    La función requiere ambos archivos de audio (file1 y file2) como argumentos de entrada y como argumento de salida entrega las metadatas de ambos archivos(audioData_1 y audioData_2).
    """
    data1, fs1 = sf.read(file1)
    data2, fs2 = sf.read(file2)
    return data1, data2

    
def convolucion(audioData_1,audioData_2):
    """
    Función que realiza dos tipos de convolución dependiendo de la cantidad de muestras de cada señal.
    Utiliza numpy y scipy para calcular cada una de las convoluciones.
    Parámetros:
    *audioData_convol: Resultado de la convolución de ambas señales.
    
    La función requiere como argumentos de entrada ambas metadatas de las señales(audioData_1 y audioData_2) y entrega los valores de amplitud de la señal resultante (audioData_convol) como argumento de salida.
    """
    if (len(audioData_1)>500) & (len(audioData_2)>500):
        audioData_convol = fftconvolve(audioData_1, audioData_2, mode='full')
    else:
        audioData_convol = np.convolve(audioData_1, audioData_2)
        
    return audioData_convol


if __name__ == "__main__":
    audioData_1, audioData_2 = cargar('RI_Sintetizada.wav', 'Mono.wav')
    convolucion(audioData_1,audioData_2)
