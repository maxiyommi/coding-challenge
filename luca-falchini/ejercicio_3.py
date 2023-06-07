from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
# Se requiere cargar un archivo de audio para extraer información que permitan caracterizar su contenido.

# 1- Cargar el archivo de audio y leer su metadata.
def read_wav(file):
    """
    Leer un archivo ".wav"
    
    Parámetros
    ----------
    file: path
        ruta del archivo

    Returns
    -------
    (int: frecuencia de muestreo, array: data de audio)
    """
    fs, audiodata = wavfile.read(file)
    return fs, audiodata

# 2- Obtener los valores máximos y mínimos.
def min_max(data):
    """
    Calcular el mínimo y el máximo de un array.
    
    Parámetros
    ----------
    data: array
        
    Returns
    -------
    (float: valor máximo, float: valor mínimo)
    """
    max_val = np.max(data)
    min_val = np.min(data)
    return max_val, min_val

# 3- Obtener el valor promedio de la señal y representarlo mediante una línea horizontal en el gráfico.
def grafico_min_max_mean(data, fs=44100, graph_name=" Señal dominio temporal "):
    """
    Función que grafica un conjunto de datos de un array y muestra su máximo, mínimo y promedio.
    
    Parámetros
    ----------
    data: array
        array de datos
    fs:
        frecuencia de muestreo
        
    graph_name: str
        nombre del gráfico

    Returns
    -------
    Gráfico con el máximo, el mínimo y el promedio.
    """
    data_norm = data/np.abs(np.max(data))    # Normalizado
    max_ind = np.argmax(data_norm)   # Indice del valor máximo
    min_ind = np.argmin(data_norm)   # Indice del valor mínimo
    avg = np.mean(np.abs(data_norm)) # Promedio
    avg_array = np.full(len(data_norm), avg) # array con valores del promedio
    n = np.linspace(0, len(data_norm)/fs, num=len(data_norm)) # linspace para plotear
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.annotate("Máximo (x;y):({};{})".format(np.round(max_ind/fs,2),np.round(np.max(data_norm),2)),
                xy=(max_ind/fs, np.max(data_norm)), xycoords='data',
                xytext=(max_ind/fs+0.2, np.max(data_norm)+0.2), textcoords='data',
                size=10, va="center", ha="center",
                bbox=dict(boxstyle="round4", fc="w"),
                arrowprops=dict(arrowstyle="-|>",connectionstyle="arc3,rad=-0.2", fc="w"))  # Indico el máximo valor
    ax.annotate("Mínimo (x;y):({};{})".format(np.round(min_ind/fs,2),np.round(np.min(data),2)),
                xy=(min_ind/fs, np.min(data_norm)), xycoords='data',
                xytext=(min_ind/fs+2, np.min(data_norm)-0.2), textcoords='data',
                size=10, va="center", ha="center",
                bbox=dict(boxstyle="round4", fc="w"),
                arrowprops=dict(arrowstyle="-|>",connectionstyle="arc3,rad=-0.2", fc="w"))  # indico el mínimo valor
    ax.annotate("Promedio (x;y):({};{})".format(np.round(len(data_norm)/fs,2), np.round(avg,2)) ,
                xy=(len(data_norm)/fs,np.round(np.min(avg),2)), xycoords='data',
                xytext=(len(data_norm)/fs+0.2,np.round(np.min(avg),2)+0.2), textcoords='data',
                size=10, va="center", ha="center",
                bbox=dict(boxstyle="round4", fc="w"),
                arrowprops=dict(arrowstyle="-|>",connectionstyle="arc3,rad=-0.2", fc="w"))  # indico el Promedio
    ax.plot(n,data_norm)
    ax.plot(n,avg_array) 
    ax.grid()
    ax.set_xlabel("Muestras")
    ax.set_ylabel("Amplitud")
    plt.title(graph_name)
    plt.show()

if __name__ == "__main__":
    # 1
    audioFileName = "luca-falchini\clarinete.wav"
    fs, audiodata = read_wav(audioFileName)
    print('AudioFile = {}, Sample Rate = {} [Samples/Sec], Wav format = {}, Samples = {}, length = {}'.format(audioFileName,fs,audiodata.dtype,audiodata.shape[0],audiodata.shape[0]/fs))

    # 2
    max_val, min_val = min_max(audiodata)
    print(max_val, min_val)   

    # 3     
    grafico_min_max_mean(audiodata, fs)
