# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:55:47 2023

@author: Agustín
"""
from numpy import convolve
from scipy.signal import fftconvolve
import soundfile as sf
def ejercicio4(audioData_1,audioData_2):
    if len(audioData_1) & len(audioData_2) >= 500:
        audioData_convol=fftconvolve(audioData_1,audioData_2)
    else:
        audioData_convol=convolve(audioData_1,audioData_2)
    return audioData_convol
    
if __name__ == "__main__":
    data1, fs= sf.read("audio (9).wav")
    data2, fs = sf.read("audio (8).wav")
    datafinal = ejercicio4(data1,data2)
    print("El resultado de la convolución es: ", datafinal)
