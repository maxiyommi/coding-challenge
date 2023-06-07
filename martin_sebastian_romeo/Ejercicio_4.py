# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:35:23 2023

@author: Martin
"""

import numpy as np
import soundfile as sf
import scipy as sp
# importo librerias


def Fun_4 (file1, file2):
   
    """
   La funcion recibe como parametros dos audios, los lee, registra sus datos, y
   permite realizar la convolucion de las señales por dos metodos distintos, dependiendo
   de la cantidad de muestras de las señales.
   Para señales con muestras mayor a 500, emplea sp.signal.fftconvolve
   Para señales con muestras menores o iguales a 500, emplea np.convolve
   
    """
    #Extraigo los datos del audio 1
    audiodata, fs = sf.read(file1, dtype='float32')
    
    #Extraigo los datos del audio 2
    audiodata_2, fs_2 = sf.read(file2, dtype='float32')
    
    #El condicional permite elegir entre una forma de convolucion o la otra dependiendo de la cantidad de muestras
    if fs>500 or fs_2>500:
        audiodata_convol = sp.signal.fftconvolve(audiodata,audiodata_2, mode = "full")
        
    else:
        audiodata_convol = np.convolve(audiodata, audiodata_2, mode = "full")
        
    return (audiodata_convol)