import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def carga_lectura_wav(nombre_archivo):
    """
    La función se encarga de leer los datos un archivo de audio. 
    Parámetros:
        nombre_archivo: se recibe el nombre del archivo a cargar y leer, o su ruta de acceso.
    Returns:
        data: se devuelven los datos del audio en forma de array.
        fs: se devuelve el valor de la frecuencia de sampleo del audio a leer.
    """

    data, fs = sf.read(nombre_archivo)

    return data, fs

def promedio_señal(archivo):
    """
    La función se encarga de leer calcular y graficar el valor promedio del audio ingresado por parámetro. 
    Parámetros:
        archivo: se recibe el nombre del archivo a calcular su promedio; o su ruta de acceso.
    Returns:
        -
    """

    data_archivo, fs_archivo = carga_lectura_wav(archivo)
    maximo = np.argmax(data_archivo)
    minimo = np.argmin(data_archivo)

    promedio = np.mean(data_archivo)

    plt.axhline(promedio, 0, len(data_archivo), color='blue', linestyle='--', label='Promedio')
    plt.title('Promedio Señal')
    plt.legend()
    plt.show()

if __name__ == '__main__':

    promedio_señal('ruido_rosa.wav')
