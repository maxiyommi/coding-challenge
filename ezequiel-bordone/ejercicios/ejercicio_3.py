'''
Ejercicio_3
Se requiere cargar un archivo de audio para extraer información que permitan caracterizar su contenido.
1. Cargar el archivo de audio y leer su metadata.
2. Obtener los valores máximos y mínimos.
3. Obtener el valor promedio de la señal y representarlo mediante una línea horizontal en el gráfico.
'''
import wave
import numpy as np
import matplotlib.pyplot as plt

# 1
def cargarLeerArchivos(audioPath):
    # Abrir el archivo de audio
    with wave.open(audioPath, 'rb') as wf:
        # Obtener información básica del archivo de audio
        channels = wf.getnchannels()
        sampleRate = wf.getframerate()
        cantidadFrames = wf.getnframes()
        
        # Leer los frames del archivo de audio
        frames = wf.readframes(cantidadFrames)
    
    # Convertir los frames a un array de numpy
    audioSignal = np.frombuffer(frames, dtype=np.int16)
    
    # Normalizar la señal de audio (si es estéreo, convertir a mono)
    if channels == 2:
        audioSignal = audioSignal[::2] + audioSignal[1::2]
        audioSignal = audioSignal / np.max(audioSignal)
    
    # Obtener la duración del archivo de audio
    duracion = cantidadFrames / sampleRate
    
    # Crear un diccionario con la metadata
    metadata = {
        'duracion': duracion,
        'sampleRate': sampleRate,
        'channels': channels,
        'cantidadFrames': cantidadFrames
    }
    
    return audioSignal, metadata

# Uso de la función
audioPath = 'clarinete.wav'
audioSignal, metadata = cargarLeerArchivos(audioPath)

# Imprimir la metadata
print("Metadata:", metadata)

# 2
def obtener_valores_maximos_y_minimos(audioSignal):
    # Obtener los valores máximos y mínimos de la señal
    valorMáximo = np.max(audioSignal)
    valorMínimo = np.min(audioSignal)
    
    return valorMáximo, valorMínimo

valorMáximo, valorMínimo = obtener_valores_maximos_y_minimos(audioSignal)

print("Valor máximo:", valorMáximo)
print("Valor mínimo:", valorMínimo)


# Calcular el valor promedio
valorPromedio = np.mean(audioSignal)

print("Valor prmedio:", valorPromedio)

# 3

# Crear el gráfico
plt.figure(figsize=(14, 5))
plt.plot(audioSignal, label='Señal de Audio')
plt.axhline(y=valorPromedio, color='r', linestyle='--', label='Valor Promedio')
plt.title('Señal de Audio con Valor Promedio')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.show()