import numpy as np
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt
import wave

def convolucion_audio(audioFile_1, audioFile_2):
    """
    Realiza la convolución de dos archivos de audio WAV.

    Parámetros:
    audioFile_1 (str): Ruta del archivo WAV del primer audio.
    audioFile_2 (str): Ruta del archivo WAV del segundo audio.

    Devuelve:
    numpy.ndarray: El resultado de la convolución de los dos audios.
    """    
    with wave.open(audioFile_1, 'rb') as wav1:
        params1 = wav1.getparams()
        audioData_1 = np.frombuffer(wav1.readframes(params1.nframes), dtype=np.int16)
        fs1 = params1.framerate  # Frecuencia de muestreo de la señal 1

    with wave.open(audioFile_2, 'rb') as wav2:
        params2 = wav2.getparams()
        audioData_2 = np.frombuffer(wav2.readframes(params2.nframes), dtype=np.int16)
        fs2 = params2.framerate  # Frecuencia de muestreo de la señal 2

    # Verificamos la longitud de las señales
    if len(audioData_1) <= 500 or len(audioData_2) <= 500:
        # Usamos numpy.convolve para señales cortas
        audioData_convol = np.convolve(audioData_1, audioData_2, mode='full')
    else:
        # Usamos scipy.signal.fftconvolve para señales largas
        audioData_convol = fftconvolve(audioData_1, audioData_2, mode='full')
    
    # Crear vector de tiempo en segundos
    tiempo1 = np.arange(len(audioData_1)) / fs1
    tiempo2 = np.arange(len(audioData_2)) / fs2
    tiempo_conv = np.arange(len(audioData_convol)) / fs1  # Suponemos misma frecuencia de muestreo para el resultado

    return audioData_1, tiempo1, audioData_2, tiempo2, audioData_convol, tiempo_conv

def plot_convolucion_audio(audioData_1, tiempo1, audioData_2, tiempo2, audioData_convol, tiempo_conv):
    """
    Grafica las señales de audio y el resultado de la convolución.

    Parámetros:
    audioData_1 (numpy.ndarray): Señal de audio 1.
    tiempo1 (numpy.ndarray): Tiempo en segundos para la señal 1.
    audioData_2 (numpy.ndarray): Señal de audio 2.
    tiempo2 (numpy.ndarray): Tiempo en segundos para la señal 2.
    audioData_convol (numpy.ndarray): Resultado de la convolución de las dos señales.
    tiempo_conv (numpy.ndarray): Tiempo en segundos para el resultado de la convolución.
    """
    plt.figure(figsize=(12, 8))

    # Señal 1
    plt.subplot(3, 1, 1)
    plt.plot(tiempo1, audioData_1)
    plt.title('Señal 1')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud')

    # Señal 2
    plt.subplot(3, 1, 2)
    plt.plot(tiempo2, audioData_2)
    plt.title('Señal 2')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud')

    # Resultado de la convolución
    plt.subplot(3, 1, 3)
    plt.plot(tiempo_conv, audioData_convol)
    plt.title('Resultado de la convolución')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud')

    plt.tight_layout()
    plt.show()

audioFile_1 = 'Sine_Sweep.wav'
audioFile_2 = 'Filtro_Inverso.wav'

audioData_1, tiempo1, audioData_2, tiempo2, audioData_convol, tiempo_conv = convolucion_audio(audioFile_1, audioFile_2)

plot_convolucion_audio(audioData_1, tiempo1, audioData_2, tiempo2, audioData_convol, tiempo_conv)