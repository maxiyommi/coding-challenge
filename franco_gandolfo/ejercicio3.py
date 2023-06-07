# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:45:58 2023

@author: Franco
"""

import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

def caracterizar_audio(archivo):
    """
    Función que carga un archivo de audio, lee su metadata, calcula sus valores mínimo y máximo, calcula su valor promedio y lo grafica junto con la señal.
    Utiliza soundfile para leer el archivo .wav, numpy para definir la variable temporal y matplotlib para graficar.
    Parámetros:
    *data: metadata del archivo de audio
    *fs: frecuencia de muestreo
    *máximo, mínimo: valores máximos y mínimos de la señal
    *promedio: valor promedio de la señal
    
    La función requiere un archivo .wav como argumento de entrada
    """
    data, fs = sf.read(archivo)
    maximo = max(data)
    minimo = min(data)
    promedio = sum(data)/len(data)
    t = np.linspace(0, data.shape[0]/fs, data.shape[0])
    plt.plot(t,data)
    plt.title("Grafico del audio")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.plot(t,promedio*t,label = "promedio")
    plt.legend()
    plt.show()
    print("el valor máximo es: ", maximo)
    print("el valor mínimo es: ", minimo)
    print("El valor promedio es: ", promedio)
    
if __name__ == "__main__":
    caracterizar_audio('RI_sintetizada.wav')