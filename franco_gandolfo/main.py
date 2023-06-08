# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:39:50 2023

@author: Franco
"""


from ejercicio1 import funcion_simbolica
from ejercicio2 import secuencia_aleatoria
from ejercicio3 import caracterizar_audio
from ejercicio4 import cargar, convolucion

funcion_simbolica()

secuencia_aleatoria()

caracterizar_audio('RI_sintetizada.wav')

audioData_1, audioData_2 = cargar('RI_Sintetizada.wav', 'Mono.wav')

convolucion(audioData_1,audioData_2)

