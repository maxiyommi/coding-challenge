from Ejercicio1 import funcion_partida
from Ejercicio1 import graficar_funcion
from Ejercicio2 import valores_aleatorios
from Ejercicio3 import info_archivo
from Ejercicio3 import grafico_archivo
from Ejercicio4 import convolucion_señales
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import fftconvolve
import sympy as sp


def main():
    
    """Ejercicio 1"""
    x = sp.Symbol('x')
    trozos = [(0, x <= 0), (x, (x > 0) & (x <= 1)), (2-(x), (x > 1) & (x < 2)), (0, x >= 2)]
    funcion_a_trozos = sp.Piecewise(*trozos)
    
    funcion_partida(x)
    graficar_funcion(funcion_a_trozos)
    
    """Ejercicio 2"""
    secuencia = np.random.randint(0,11,size=30)
    v_a = valores_aleatorios(secuencia)
    
    """Ejercicio 3"""
    archivo = "sine_sweep.wav"
    info_archivo(archivo)
    grafico_archivo(archivo)
    
    """Ejercicio 4"""
    archivo_1 = "ruido_rosa.wav"
    archivo_2 = "sine_sweep.wav"
    convolucion_señales(archivo_1, archivo_2)
    
if __name__=="__main__":
    main()