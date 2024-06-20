'''
Ejercicio_4
Crear una función para aplicar la convolución entre dos señales de audio (Por ejemplo usando [numpy.convolve](https://numpy.org/doc/1.19/reference/generated/numpy.convolve.html) y [scipy.signal.fftconvolve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html#scipy.signal.fftconvolve)). La función debe ser capaz de elegir un método u otro en función de la cantidad de muestras de cada señal(> 500).

Debe cumplir con: 
* Dos argumentos de entrada como mínimo: audioData_1 (valores de amplitud de la señal 1) y audioData_2 (valores de amplitud de la señal 2).
* Un argumento de salida: convolucionNoise (valores de amplitud de la señal resultante de la convolución)
'''

import numpy as np
import scipy.signal as sp
import soundfile as sf

def convolucion(audioData1, audioData2):

    audio1, sampleRate1 = sf.read(audioData1)
    audio2, sampleRate2 = sf.read(audioData2)

    if sampleRate1 != sampleRate2:
        raise ValueError("Los archivos tienen distinta tasa de muestreo")

    if len(audio1) < '500':
        impulso = sp.fftconvolve(audio1, audio2, mode='full')
    else:
        impulso = np.convolve(audio1, audio2, mode='full')

    sf.write("convolucion.wav", impulso, sampleRate1)

    return impulso

# Ejemplo de uso
audioData1 = 'pinkNoise.wav'
audioData2 = 'whiteNoise.wav'
convolucionNoise = convolucion(audioData1, audioData2)