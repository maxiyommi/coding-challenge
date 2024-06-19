import numpy as np
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt

def convolve(audioData_1, audioData_2):
    """
    Aplica la convolución entre dos señales de audio utilizando np.convolve o scipy.signal.fftconvolve
    según la cantidad de muestras de cada señal.

    Args:
    - audioData_1 (array-like): Valores de amplitud de la señal 1.
    - audioData_2 (array-like): Valores de amplitud de la señal 2.

    Returns:
    - audioData_convol (array): Valores de amplitud de la señal resultante de la convolución.
    """
    if len(audioData_1) > 500 or len(audioData_2) > 500:
        audioData_convol = fftconvolve(audioData_1, audioData_2, mode='full')
    else:
        audioData_convol = np.convolve(audioData_1, audioData_2, mode='full')

    return audioData_convol

fs = 1000 
t = np.linspace(0, 1, fs) 
freq1 = 5  
freq2 = 20 

signal_1 = np.sin(2 * np.pi * freq1 * t)  
signal_2 = np.cos(2 * np.pi * freq2 * t)  

convolution_result = convolve(signal_1, signal_2)


plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, signal_1, label='Señal 1')
plt.title('Señales Originales')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, signal_2, label='Señal 2')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()

plt.subplot(3, 1, 3)

t_conv = np.linspace(0, 2 - 1/fs, len(convolution_result))
plt.plot(t_conv, convolution_result, label='Resultado de la Convolución', color='r')
plt.title('Resultado de la Convolución')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()

plt.tight_layout()
plt.show()