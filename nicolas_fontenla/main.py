from sympy.plotting import plot
import soundfile as sf
from ejercicio_1 import f_trozos, calculo_energia_potencia
from ejercicio_2 import secuencia_aleatoria
from ejercicio_3 import lectura_audio, max_min_prom
from ejercicio_4 import convolucion

#Resolucion del ejercicio 1
energia_potencia = calculo_energia_potencia(f_trozos)
plot(f_trozos, line_color='red', title='Funcion por partes', xlim=(-2,3))

#Resolucion del ejercicio 2
secuence = secuencia_aleatoria()

#Resolucion ejercicio 3
audio = 'S1R2_M30.wav'
data, fs = lectura_audio(audio) 
maximo, minimo, promedio = max_min_prom(data, fs)


print('El valor maximo de la señal es: ', maximo)
print('El valor minimo de la señal es: ', minimo)
print('El valor promedio de la señal es: ', promedio)

#Resolucion ejercicio 4
audio_1, fs = sf.read("sine-sweep.wav",dtype='float32')
audio_2, fs = sf.read("inverse-filter.wav",dtype='float32')
datafinal = convolucion(audio_1,audio_2)
print('El resultado de la convolucion es: ',datafinal)
sf.write('Convolucion.wav',datafinal, 44100)
