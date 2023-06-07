# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:05:19 2023

@author: Agustín
"""
from ejercicio_1 import ejercicio1
from ejercicio_2 import ejercicio2
from ejercicio_3 import ejercicio3
from ejercicio_4 import ejercicio4
import soundfile as sf

if __name__=="__main__":
    Funcion,Energia,Potencia = ejercicio1()
    print("Ejercicio 1:")
    display(Funcion)
    print ("La energía es: ",Energia) 
    print("La potencia es: ", Potencia)
    valor_max_2, valor_min_2, ind_max, ind_min = ejercicio2()
    print("Ejercicio 2:")
    print("los indices con el valor maximo (", valor_max_2, "), son: ", ind_max)
    print("los indices con el valor minimo (", valor_min_2, "), son: ", ind_min)
    valor_max_3, valor_min_3, prom = ejercicio3("audio1.wav")  
    print("Ejercicio 3:")
    print("El valor máximo es: ", valor_max_3)
    print("El valor minimo es: ", valor_min_3)
    print("El valor promedio es: ",prom)
    data1, fs= sf.read("audio1.wav")
    data2, fs = sf.read("audio2.wav")
    datafinal = ejercicio4(data1,data2)
    print("Ejercicio 4:")
    print("El resultado de la convolución es: ", datafinal)