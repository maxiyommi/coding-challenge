from sympy import symbols, Piecewise, integrate, oo, limit, pprint
from sympy.plotting import plot
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import fftconvolve
from scipy.fftpack import fft, ifft
from ejercicio_1 import funcion_a_trozos, grafico_funcion, energia_señal, potencia_señal
from ejercicio_2 import aleatorios
from ejercicio_3 import promedio_señal
from ejercicio_4 import carga_lectura_wav, convolucion

def main():
    print("En el presente trabajo, presentamos las respuestas de los ejercicios solicitados:\n")
    print(f"Ejercicio 1:\n{'-'*30}")
    
    x, T = symbols("x T")

    funcion = funcion_a_trozos(x)
    grafico_funcion(funcion)
    energia = energia_señal(funcion, x)
    potencia = potencia_señal(funcion, x, T)
    print("La señal está caracterizada por: ")
    pprint(funcion)
    print(
        f"\nLa misma tiene una energía de valor {energia}\nY una potencia igual a {potencia}"
    )

    print('-'*30)

    print(f"Ejercicio 2:\n{'-'*30}")
    print("Se mostrará un gráfico correspondiente a la consigna solicitada:\n")
    aleatorios(0, 10, 30)
    print('-'*30)

    print(f"Ejercicio 3:\n{'-'*30}")
    nombre_archivo_ej3 = input("Ingrese el nombre del archivo de audio seguido de .wav para graficar su promedio: ")
    promedio_señal(nombre_archivo_ej3)
    print('-'*30)

    print(f"Ejercicio 4:\n{'-'*30}")
    nombre_archivo_ej4_1 = input("Ingrese el nombre del primer archivo de audio seguido de .wav para convolucionar (o su ruta de acceso): ")
    nombre_archivo_ej4_2 = input("Ingrese el nombre del segundo archivo de audio seguido de .wav para convolucionar (o su ruta de acceso): ")
    data_1, fs_1 = carga_lectura_wav(nombre_archivo_ej4_1)
    data_2, fs_2 = carga_lectura_wav(nombre_archivo_ej4_2)
    convolucion_audios = convolucion(data_1, data_2)
    print('-'*30)

if __name__ == '__main__':
    main()