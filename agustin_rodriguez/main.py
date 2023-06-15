#Se importan todas las funciones
from Ejercicio_1 import calcular_caracteristicas_funcion
from Ejercicio_2 import graficar_secuencia_aleatoria
from Ejercicio_3 import graficar_valor_promedio_audio
from Ejercicio_4 import convolucion
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

#Se corren todas las funciones

#Ejercicio_1
calcular_caracteristicas_funcion()

#Ejercicio_2
graficar_secuencia_aleatoria()

#Ejercicio_3
archivo_audio = 'clarinete.wav'
graficar_valor_promedio_audio(archivo_audio)

#Ejercicio_4
audioData_1, fs_1 = sf.read('impulso.wav')
audioData_2, fs_2 = sf.read('ruido_rosa.wav')
resultado_convolucion = convolucion(audioData_1, audioData_2)
plt.plot(resultado_convolucion)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Convolución entre audioData_1 y audioData_2')
plt.show()