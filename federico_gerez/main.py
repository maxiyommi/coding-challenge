# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:45:51 2023

@author: Usuario
"""

from Ejercicio_1 import funcion, graficar_funcion, energia_señal, potencia_señal, x
from Ejercicio_2 import secuencia_aleatoria, indice_max_min, graficar_secuencia
from Ejercicio_3 import lectura_wav, maximo_minimo, grafico_valor_promedio
from Ejercicio_4 import convolucion_señales

#Ejercicio 1
salida = funcion(x) 
graficar_funcion(salida)
energia_señal(salida)
potencia_señal(salida)

#Ejercicio 2
secuencia = secuencia_aleatoria(30)
indice_maximo, indice_minimo = indice_max_min(secuencia)
graficar_secuencia(secuencia, indice_maximo, indice_minimo)

#Ejercicio 3
data, fs = lectura_wav('sine_sweep.wav')
maximo_minimo(data)
grafico_valor_promedio(data)

#Ejercicio 4
data1, fs1 = lectura_wav('sine_sweep.wav')
data2, fs2 = lectura_wav('impulso.wav')
convolucion_señales(data1, data2)