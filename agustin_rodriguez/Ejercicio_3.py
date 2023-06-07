import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

def graficar_valor_promedio_audio(archivo_audio):
    """
    Carga un archivo de audio, lee sus datos y grafica el valor promedio de la señal en función del tiempo.

    Args:
        archivo_audio (str): Ruta del archivo de audio a cargar.

    Returns:
        None

    Carga el archivo de audio utilizando la librería soundfile. Luego, calcula el valor promedio
    de la señal y crea un array de tiempo utilizando la libreria numpy. Finalmente, crea un gráfico donde se muestra el valor
    promedio constante en función del tiempo usando la libreria matplotlib.

    El gráfico muestra en el eje x el tiempo en segundos y en el eje y el valor promedio de la señal.
    """
    # Cargar el archivo de audio y leer los datos
    data, fs = sf.read(archivo_audio)

    # Obtener el valor promedio de la señal
    promedio = np.mean(data)

    # Crear un array de tiempo en segundos para el gráfico de promedio
    tiempo = np.arange(len(data)) / fs

    # Graficar el valor promedio en función del tiempo
    plt.plot(tiempo, np.full_like(data, promedio), color='black', linestyle='-', label='Valor promedio')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud')
    plt.title('Valor promedio del audio')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    # Cargar un archivo de audio
    archivo_audio = 'clarinete.wav'
    graficar_valor_promedio_audio(archivo_audio)

