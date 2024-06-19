from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

def metadata(ruta):
    """
    Carga un archivo de audio WAV y devuelve la duración, valor máximo y mínimo de la señal.
    
    Args:
    - ruta (str): Ruta al archivo de audio WAV.
    
    Returns:
    - duracion (float): Duración del audio en segundos.
    - max_value (float): Valor máximo de la señal de audio.
    - min_value (float): Valor mínimo de la señal de audio.
    """
    # Cargar el archivo de audio
    sr, y = wavfile.read(ruta)
    
    # Calcular duración del audio
    duracion = len(y) / float(sr)
    
    # Obtener valores máximos y mínimos
    valor_max = np.max(np.abs(y))
    valor_min = -valor_max
    
    return duracion, valor_max, valor_min

def calcular_promedio(y):
    """
    Calcula el valor promedio de la señal de audio.
    """
    valor_promedio = np.mean(y)
    return valor_promedio

def plot_signal(tiempo, y, valor_promedio, sr):
    """
    Grafica la señal de audio junto con su valor promedio.

    Args:
    - tiempo (numpy.ndarray): Tiempo en segundos.
    - y (numpy.ndarray): Señal de audio.
    - valor_promedio (float): Valor promedio de la señal de audio.
    - sr (int): Tasa de muestreo del audio.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(tiempo, y, label='Señal de audio')
    plt.axhline(valor_promedio, color='g', label='Valor promedio')
    plt.title('Señal de audio y valor promedio')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.show()

archivo_audio = 'RuidoRosa.wav'
sr, y = wavfile.read(archivo_audio)
duracion, valor_max, valor_min = metadata(archivo_audio)
tiempo = np.arange(len(y)) / float(sr)
valor_promedio = np.mean(y)
valor_promedio = calcular_promedio(y)

plot_signal(tiempo, y, valor_promedio, sr)

print(f'Valor promedio: {valor_promedio:.2f}')
print(f'Valor máximo: {valor_max:.2f}')
print(f'Valor mínimo: {valor_min:.2f}')
print(f'Duración del audio: {duracion:.2f} segundos')