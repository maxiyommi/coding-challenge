import soundfile as sf
import numpy as np
from scipy import signal
from carga_archivos import lectura_wav

def convolucion(audio1, audio2, fs=44100):
    """
    Convoluciona dos archivos de audio cargados y genera un archivo wav con el array de la convolución.

    Parámetros
    ----------
    audio1 : str
        Nombre del archivo de audio 1.

    audio2 : str
        Nombre del archivo de audio 2.

    fs : int
        Frecuencia de muestreo de las señales. 44100 por defecto.

    Returns
    -------
    convol : numpy array
        Array con la información de la convolución.

    """

    data1, fs_audio1 = lectura_wav(audio1)
    data2, fs_audio2 = lectura_wav(audio2)

    if len(data1) < 500 and len(data2) < 500:
        convol = np.convolve(data1, data2)
    else:
        convol = signal.fftconvolve(data1, data2)

    sf.write("convolución.wav", convol, fs)
    return convol


   


if __name__ == "__main__":
    from grafico_señal import grafico

    conv = convolucion("filtro_inverso.wav", "ruido_rosa.wav")
    grafico(conv)
 


