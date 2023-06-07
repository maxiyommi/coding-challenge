# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:03:04 2023

@author: Martin
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
# importo librerias

def Fun_3():
    #Cargo el archivo de audio
    filename = r"C:\Users\Martin\OneDrive\Escritorio\coding-challenge-master\coding-challenge-master\Silbidos Tursiops.wav"

    #Extraigo los datos del audio
    data, fs = sf.read(filename, dtype='float32')  

    #Busco los valores maximos y minimos
    v_max = np.max(data)
    v_min = np.min(data)

    #Obtengo el valor promedio de la señal
    v_mean = np.mean(data)

    #Grafico la señal
    tiempo = len(data)/fs
    t = np.linspace(0, tiempo, num = len(data)) #Objeto numpy para la duracion del eje x (tiempo)
    fig = plt.figure()
    plt.plot(t,data)

    #Configuro el ploteo
    plt.title("Grafico del audio")
    plt.xlabel("Tiempo (seg)")
    plt.ylabel("amplitud")
    plt.axhline(y=v_mean, color = "r", label= f"Promedio ={v_mean}") #Agrego la linea horizontal en el valor promedio
    plt.legend(loc = "best") #Agrego la leyenda, haciendo que elija la mejor posicion donde ubicarse

    maxi = print("El valor maximo es =",v_max)
    mini = print("El valor minimo es =",v_min)
    
    return(maxi, mini)
