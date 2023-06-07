import soundfile as sf
from scipy.signal import fftconvolve
from scipy.fftpack import fft, ifft
import numpy as np

def carga_lectura_wav(filename):
    """
    La función se encarga de leer los datos un archivo de audio. 
    Parámetros:
        nombre_archivo: se recibe el nombre del archivo a cargar y leer, o su ruta de acceso.
    Returns:
        data: se devuelven los datos del audio en forma de array.
        fs: se devuelve el valor de la frecuencia de sampleo del audio a leer.
    """

    data, fs = sf.read(filename)

    return data, fs

def convolucion(data_1, data_2):
    """
    La función se encarga de convolucionar dos señales, por medio de sus datos ingresados.
    Parámetros:
        data_1: de tipo array, se ingresan los datos del audio 1.
        data_2: de tipo array, se ingresan los datos del audio 2.
    Returns:
        convolucion_real: se devuelve un array con los datos de la convolución obtenida entre los dos audios ingresados. 
    """

    if (len(data_1) <= 500 and len(data_2) <= 500):
        audio_convolucion = np.convolve(data_1, data_2)

    elif(len(data_1) > 500 or len(data_2) > 500):
        audio_convolucion = fftconvolve(data_1, data_2)

    convolucion_real = []

    for n in audio_convolucion:
        Re_imp = np.real(n)
        convolucion_real.append(Re_imp)

    return convolucion_real

if __name__ == '__main__':

    data_1, fs_1 = carga_lectura_wav('sine_sweep.wav')
    data_2, fs_2 = carga_lectura_wav('filtro_inverso.wav')

    convolucion_audios = convolucion(data_1, data_2)