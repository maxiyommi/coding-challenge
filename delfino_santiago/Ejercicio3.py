# -*- coding: utf-8 -*-
"""
La función devuelve información sobre la metadata de un archivo de audio, su valor máximo, 
mínimo y promedio. Y una gráfica con el valor promedio. 
---------
archivo: archivo de audio establecido
data: mediante el metodo de soundfile read se devuelve un array de valores
data_1: mediante el metodo de soundfile info se devuelve informacion sobre el tipo de archivo


"""

import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt 
from scipy.io import wavfile

archivo = "sine_sweep.wav"

def info_archivo(archivo):


    data, tasa_muestreo = sf.read("sine_sweep.wav")
    data_1 = sf.info("sine_sweep.wav",verbose=False)
    amplitudes = data.flatten()
    maximo = max(amplitudes)
    minimo = min(amplitudes)
    promedio = sum(data)/len(data)

    print(data)
    print(data_1)
    print("El valor máximo de la señal es:",maximo)
    print("El valor mínimo de la señal es:",minimo)
    print("El valor promedio de la señal es:",promedio)
    return data, data_1, maximo, minimo, promedio
info_archivo(archivo)

def grafico_archivo(archivo):
    
    fs, data = wavfile.read(archivo)
    plt.rcParams['figure.figsize'] = (15, 5) # Definir el tamaño de graficas
    # Definir los valores de los datos de amplitud entre [-1 : 1] Audiodata.dtype es int16
    dataScaled = data/(2**15)

    #definir los valores del eje x en milisegundos
    timeValues = np.arange(0, len(dataScaled), 1)/ fs # Convertir Muestras/Seg a Segundos
    timeValues = timeValues * 1000  #Escala de tiempo en milisegundos
    
    promedio = sum(data)/len(data)
    grafico=plt.plot(timeValues, dataScaled);plt.title('Archivo en dominio temporal',size=16)
    plt.text(0-100, promedio, 'Promedio', fontsize = 16,bbox=dict(facecolor='green', alpha=0.5))
    plt.ylabel('Amplitud'); plt.xlabel('Tiempo (ms)');
    return grafico

grafico_archivo(archivo)    

if __name__ == "__main__":
    
    audio = info_archivo(archivo)
    grafica = grafico_archivo(archivo)
