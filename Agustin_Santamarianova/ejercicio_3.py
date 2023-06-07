# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:21:52 2023

@author: Agustín
"""
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

def ejercicio3(file):
    data, fs = sf.read(file)
    maximo = max(data)
    minimo = min(data)
    promedio = np.mean(data)
    grafico_ej3(data,promedio,fs)
    return maximo, minimo, promedio


def grafico_ej3(data,promedio,fs):
    t = np.linspace(0., data.shape[0]/fs, data.shape[0])
    plt.title("Ejercicio 3")
    plt.plot(t,data,label="señal")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.axhline(y=promedio, color='r', linestyle='--', label="valor promedio")
    plt.legend()
    plt.show()
    plt.figure()

if __name__ == "__main__":    
    valor_max, valor_min, prom = ejercicio3("audio (9).wav")   
    print("El valor máximo es: ", valor_max)
    print("El valor minimo es: ", valor_min)
    print("El valor promedio es: ",prom)
