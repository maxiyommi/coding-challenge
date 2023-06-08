import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


# Ejercicio 3
# Usaré la librería sounfile
# Ruta al archivo de audio
ruta_archivo = 'Archivo_para_Parcial.wav'

# Cargar archivo de audio
audio, sr = sf.read(ruta_archivo)

# Leer metadatos
info = sf.info(ruta_archivo)

# Imprimir los metadatos
print("Metadatos del archivo de audio:")
print(info)
# Se obtienen los valores máximos y mínimos sobre la variable audio y se imprimen
valor_maximo = max(audio)
valor_minimo = min(audio)
print("El valor máximo del archivo es:", valor_maximo)
print("El valor mínimo del archivo es:", valor_minimo)

# Para el valor promedio de la señal utilizé la librería Numpy
valor_promedio = np.mean(audio)
print("Valor promedio de la señal:", valor_promedio)

##### Configuración para el eje x
rate = len(audio)
time = np.linspace(0, rate/sr, num=rate)
#####

# Grafico el valor promedio junto con la señal de audio en color rojo
plt.plot(time, audio,)
plt.axhline(valor_promedio, color='r')
plt.xlabel('Duración [s]')
plt.ylabel('Amplitud')
plt.title('Archivo para Parcial')
plt.grid(True)
plt.show()
