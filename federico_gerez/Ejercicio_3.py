# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:08:53 2023

@author: Usuario
"""
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

def lectura_wav(filename):
    """
    Lee un archivo de audio .wav ingresado.

    Parametros
    ----------
    filename : archivo de audio.

    Returns
    -------
    data : numpy array
        Data del archivo de audio.

    fs: int
        Frecuencia de muestreo del audio en hz.
    """

    data, fs = sf.read(filename)
    return data, fs

def maximo_minimo(data):
    """
    Obtiene los valores máximo y mínimo de una señal de datos.

    Parameters
    ----------
    data : numpy array
        Data del archivo de audio.

    Returns
    -------
    max_value : float
        valor máximo de la señal.
    min_value : float
        valor mínimo de la señal.

    """
    # Obtener los valores máximos y mínimos
    max_value = np.max(data)
    min_value = np.min(data)

    # Imprimir los valores máximos y mínimos
    print("Valor máximo:", max_value)
    print("Valor mínimo:", min_value)
    return max_value, min_value

def grafico_valor_promedio(data, fs=44100):
    """
    Grafica una señal de datos y muestra una línea horizontal en el valor promedio.

    Parameters
    ----------
    data : numpy array
        data del archivo de audio.

    Returns
    -------
    grafico de la señal de datos, con una linea horizontal en el valor promedio

    """
    # Obtener el valor promedio
    average_value = np.mean(data)
    print("El valor promedio es: ", average_value)
    
    # Crear la figura y el objeto de los ejes
    fig, ax = plt.subplots()
    
    # Calcular el tiempo correspondiente a cada muestra
    time = np.arange(len(data)) / fs
    
    # Graficar la señal de audio
    ax.plot(time, data)
    
    # Dibujar una línea horizontal para el valor promedio
    ax.axhline(y=average_value, color='r', linestyle='--', label='Promedio')
    
    # Personalizar los ejes y el título
    ax.set_xlabel('Tiempo(s)')
    ax.set_ylabel('Amplitud')
    ax.set_title('Gráfico de la señal de audio')
    
    # Agregar una leyenda
    ax.legend()
    
    return plt.show()

if __name__ == '__main__':
    data, fs = lectura_wav('sine_sweep.wav')
    maximo_minimo(data)
    grafico_valor_promedio(data)
