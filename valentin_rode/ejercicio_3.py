import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

# Carga del archivo de audio
def cargar_audio(ruta_archivo):
    """
    Loads an audio file and returns the audio signal and its sampling rate.

    Args:
        ruta_archivo (str): Path to the audio file.

    Returns:
        tuple: A tuple containing the audio signal and the sampling rate of the file.

    """
    audio_array, sample_rate = sf.read(ruta_archivo)

    return audio_array, sample_rate

# Extracción de información de la señal de audio
def max_min_mean(audio_array, sample_rate): 
    """
    Calculates the maximum, minimum, mean, and duration of an audio signal represented by a NumPy array.

    Args:
        audio_array (numpy.ndarray): The audio signal as a NumPy array.
        sample_rate (float): The sampling rate of the audio signal in Hz.

    Returns:
        tuple: A tuple containing the maximum, minimum, mean, and duration values of the audio signal.
    """
    duracion = len(audio_array) / sample_rate

    max = np.max(audio_array)
    min = np.min(audio_array)

    mean = np.mean(audio_array)

    return mean

def get_plot(audio_array, sample_rate,mean):
    """
    Generates a plot of an audio signal along with its mean value.

    Args:
        audio_array (numpy.ndarray): The audio signal as a NumPy array.
        sample_rate (float): The sampling rate of the audio signal in Hz.
        mean (float): The mean value of the audio signal.

    """
    duracion = len(audio_array) / sample_rate
    recta=np.full(len(audio_array),mean)
    t = np.linspace(0, duracion, len(audio_array))

    plt.plot(t, audio_array)
    plt.plot(t,recta)
    plt.legend(["Señal de audio","Recta promedio"])
    # Etiquetas y título
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    # Leyenda
    

    # Visualización de la gráfica
    plt.show()

if __name__=="__main__":
    ruta_archivo = "IR_Hall_example 3.wav"
    # Carga y procesamiento de la señal de audio
    audio_array, fs = cargar_audio(ruta_archivo)
    mean= max_min_mean(audio_array,fs)
    # Generación de la gráfica
    get_plot(audio_array, fs , mean)
