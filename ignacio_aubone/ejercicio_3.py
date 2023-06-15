import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import os

def caracterizar_audio(filename):
    """
    Carga un archivo de audio y brinda información para caracterizar su contenido.

    Parámetros
    ----------
    filename : str
        Nombre del archivo de audio en formato WAV.

    Nota
    ----
    La función no tiene returns.
    Al llamarla, realiaza lo siguiente:
            - Imprime los valores de amplitud máxima y mínima de la señal.
            - Imprime el valor de amplitud promedio de la señal.
            - Genera un gráfico de la señal resaltando el valor promedio.

    """
    # Carga del archivo de audio y lectura de su metadata
    data, fs = sf.read(filename)
    
    # Obtención de los valores máximo y mínimo
    maximo = np.max(data)
    minimo = np.min(data)
    
    # Obtención del valor promedio de la señal
    promedio = np.mean(np.abs(data))
    
    # Impresión de los valores característicos
    print('Amplitud máxima:', maximo)
    print('Amplitud mínima:', minimo)
    print('Amplitud promedio:', promedio)
    
    # Calcular la duración en segundos
    duracion = len(data) / fs

    # Generar el arreglo de valores para el eje x
    tiempo = np.linspace(0, duracion, len(data))
    
    # Gráfico de la señal
    plt.plot(tiempo, data, label='Señal de audio')
    plt.axhline(promedio, color='r', linestyle='--', label='Valor promedio')
    plt.xlabel('Tiempo (s)', fontsize=14)
    plt.ylabel('Amplitud', fontsize=14)
    plt.legend()
    plt.show()
    
