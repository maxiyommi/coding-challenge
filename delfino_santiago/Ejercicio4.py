# -*- coding: utf-8 -*-
"""
La función realiza la convolución entre dos archivos de audio ya fijados. 
---------
archivo_1:  primer archivo fijado
archivo_2: Ídem segundo

Se utiliza la librería soundfile para la carga y lectura de los archivos (Con el método sf.read) 
Luego mediante la librería Numpy convertimos en arrays los archivos de audio.
De esta forma nos  será posible poder realizar la convolución mediante fftconvolve de Scipy
y np.convolve de Numpy.
Además se usan los métodos sf.info e info.frames para poder armar un condicional donde si el archivo de audio
es mayor a 500 muestras se opta por la convolución a través de fftconvolve de Scipy.
Caso contrario se la realiza a través de Numpy.

"""

import numpy as np
from scipy.signal import fftconvolve
import soundfile as sf

archivo_1 = "ruido_rosa.wav"
archivo_2 = "sine_sweep.wav"

def convolucion_señales(archivo_1,archivo_2):
    audio, samplerate = sf.read(archivo_1)
    audio_1, samplerate = sf.read(archivo_2)
    audio_array = np.array(audio)
    audio_1_array = np.array(audio_1)
    info = sf.info(archivo_1)
    info_1 = sf.info(archivo_2)
    num_muestras = info.frames
    num_muestras_1 = info_1.frames
    
    if num_muestras or num_muestras_1 > 500:
        convolucion_fft = fftconvolve(audio_array,audio_1_array)
        print(convolucion_fft)
    
    else:
        convolucion_np = np.convolve(audio_array, audio_1_array)
        print(convolucion_np)
        
    return convolucion_fft

convolucion_señales(archivo_1, archivo_2)

if __name__ == "__main__":
    
    operacion = convolucion_señales(archivo_1, archivo_2)