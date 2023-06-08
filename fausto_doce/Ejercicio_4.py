import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import scipy

# Ejercicio 4
# Si n cantidad de muestras de la señal es n>500, se aplicará  scipy.signal.fftconvolve, sino se aplicará numpy.convolve)
# Se leen los 2 archivos de audio por sound file. Para que se aplique scipy.signal.fftconvolve ambas señales deben contar con más de 500 muestras. Si tanto audio1 o audio2 tienen menos de 500 muetras, se aplicará numpy.convolve

def convolucion_audio(ruta_archivo1, ruta_archivo2):
    audio1, sr1 = sf.read(ruta_archivo1)
    audio2, sr2 = sf.read(ruta_archivo2)
    if sr1<500 or sr2<500:
        convolución = np.convolve(audio1, audio2)
    elif sr1>500 and sr2>500:
        convolución = scipy.signal.fftconvolve(audio1, audio2, mode='full', axes=None)
    return convolución

# Ejemplo con 2 archivos de audio

Conv1_2=convolucion_audio('Archivo_para_Parcial.wav','Archivo_para_parcial2.wav')

##### Configuración para el eje x
sr = 44100
rate12 = len(Conv1_2)
time12 = np.linspace(0, rate12/sr, num=rate12)
#####

# Se plotea el ejemplo
plt.plot(time12, Conv1_2)
plt.xlabel('Duración [s]')
plt.ylabel('Amplitud')
plt.title('Convolución')
plt.grid(True)
plt.show()