import numpy as np
import soundfile as sf


def lectura_wav(filename):
    """
    Lee un archivo de audio .wav ingresado.

    Parametros
    ----------
    filename : archivo de audio.

    Returns
    -------
    data : numpy array
        Data del archivo de audio.

    fs: int
        Frecuencia de muestreo del audio en hz.
    """

    data, fs = sf.read(filename)

    return data, fs


def carga_wav(archivos):
    """
    Almacena los datos de los archivos de audioingresados.

    Parameters
    ----------
    archivos : lista
        Lista con los nombres de los archivos de audio.

    Returns
    -------
    audios : dict
        Diccionario que tiene los nombres de los archivos de audio como keys y como values una tupla que contiene el array de información del audio seguido por su frecuencia de muestreo (int).

    """
    archivos = np.array(archivos)
    audios = {}
    for i in range(archivos.size):
        data, fs = lectura_wav(archivos[i])
        audios[archivos[i]] = data, fs
    return audios


if __name__ == "__main__":
    from grafico_señal import grafico

    audios = carga_wav(["RI_1.wav", "RI_2.wav"])
    data_RI1, fs_RI1 = audios.get("RI_1.wav")
    data_RI2, fs_RI2 = audios.get("RI_2.wav")
    grafico(data_RI1)
    grafico(data_RI2)
