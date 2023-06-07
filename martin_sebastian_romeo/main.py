# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:54:40 2023

@author: Martin
"""
#Importo a las funciones de los ejercicios
from Ejercicio_1 import Fun_1
from Ejercicio_2 import Fun_2
from Ejercicio_3 import Fun_3
from Ejercicio_4 import Fun_4


    
if __name__ == "__main__":
    #Elijo los archivos de audio para cargar en la funcion 4
    filename_1 = r"C:\Users\Martin\OneDrive\Escritorio\coding-challenge-master\coding-challenge-master\InvFilter.wav"
    filename_2 = r"C:\Users\Martin\OneDrive\Escritorio\coding-challenge-master\coding-challenge-master\record_SineSweepLog.wav"
    
    #Llamo a las funciones
    Fun_1()
    Fun_2()
    Fun_3()
    Fun_4(filename_1, filename_2)
    

    
    