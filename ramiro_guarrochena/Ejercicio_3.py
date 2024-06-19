import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

def cargar_audio(ruta):
    try:
        audio, fs = sf.read(ruta)
        duracion = len(audio) / fs
        
        # Calcular promedio de la magnitud absoluta de la señal
        promedio = np.mean(np.abs(audio))
        
        # Encontrar tiempo de máximo y mínimo en segundos
        tiempo_max = np.argmax(np.abs(audio)) / fs
        tiempo_min = np.argmin(np.abs(audio)) / fs
        
        # Imprimir resultados
        print("Frecuencia de muestreo:", fs, "Hz")
        print("Duración:", duracion, "segundos")
        print("Máximo en:", tiempo_max, "segundos")
        print("Mínimo en:", tiempo_min, "segundos")
        print("Promedio de la magnitud absoluta de la señal:", promedio)
        
        # Graficar la forma de onda de la señal y las líneas de tiempo
        tiempo = np.arange(0, len(audio)) / fs
        
        plt.figure(figsize=(12, 6))
        plt.plot(tiempo, audio, label='Forma de onda')
        plt.axhline(y=promedio, color='r', linestyle='--', label='Promedio')
        plt.axvline(x=tiempo_max, color='g', linestyle='--', label='Máximo')
        plt.axvline(x=tiempo_min, color='b', linestyle='--', label='Mínimo')
        
        plt.xlabel('Tiempo [segundos]')
        plt.ylabel('Amplitud')
        plt.title('Forma de onda del archivo de audio con líneas de tiempo y promedio')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
        # Retornar valores calculados
        return fs, duracion, tiempo_max, tiempo_min, promedio
    
    except Exception as e:
        print("Error al leer el archivo:", e)
        return None, None, None, None, None  # En caso de error, retornar valores nulos o None

if __name__ == "__main__":
    # Ejemplo de uso de la función cargar_audio
    ruta_archivo = r"C:\Users\ramag\Desktop\Grabacion II\TP1\Archivos multipista\12_Violin1.wav"
    fs, duracion, tiempo_max, tiempo_min, promedio = cargar_audio(ruta_archivo)

    # Aquí puedes utilizar los valores calculados fuera de la función si es necesario
    if fs is not None:
        print("Frecuencia de muestreo fuera de la función:", fs, "Hz")
        print("Duración fuera de la función:", duracion, "segundos")
        print("Máximo tiempo fuera de la función:", tiempo_max, "segundos")
        print("Mínimo tiempo fuera de la función:", tiempo_min, "segundos")
        print("Promedio fuera de la función:", promedio)
