# Crear una función para aplicar la convolución entre dos señales de audio (Por ejemplo usando numpy.convolve y scipy.signal.fftconvolve). 
# La función debe ser capaz de elegir un método u otro en función de la cantidad de muestras de cada señal(> 500).

# Debe cumplir con:

# Dos argumentos de entrada como mínimo: audioData_1 (valores de amplitud de la señal 1) y audioData_2 (valores de amplitud de la señal 2).
# Un argumento de salida: audioData_convol (valores de amplitud de la señal resultante de la convolución)

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from ejercicio_3 import read_wav
from ejercicio_3 import grafico_min_max_mean

def convolucion(audio1, audio2):
    """
    Aplicar la convolución entre dos señales de audio.
    ...Nota: Si las dos señales tienen menos de 500 muestras aplica el método numpy.convolve
    ...caso contrario aplica el método scipy.signal.fftconvolve
    
    Parámetros
    ----------
    audio1: array
        datos del primer audio
    
    audio2: array
        datos del segundo audio

    Returns
    -------
    conv: array
        convoluvión entre los audios.  
    """
    if len(audio1)<500 and len(audio2)<500:
         conv = np.convolve(audio1, audio2)
    else:
        conv = signal.fftconvolve(audio1, audio2)
    conv = conv/np.abs(np.max(conv))    # Normalizado
    return conv


if __name__ == "__main__":
    fs, audio1 = read_wav('luca-falchini/clarinete.wav')
    fs2, audio2 = read_wav('luca-falchini/Mono.wav')
    audio_conv = convolucion(audio1, audio2)
    grafico_min_max_mean(audio_conv, fs2, "Convolución")
    print(audio_conv)
