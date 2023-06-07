import soundfile as sf
import numpy as np
from scipy.signal import fftconvolve

def convolucion_audio(audioData_1, audioData_2):
    """
    Aplica la convolución entre dos señales de audio.

    Parámetros
    ----------
    audioData_1 : numpy.ndarray
        Valores de amplitud de la señal 1.
    audioData_2 : numpy.ndarray
        Valores de amplitud de la señal 2.

    Returns
    -------
    audioData_convol : numpy.ndarray
        Valores de amplitud de la señal resultante de la convolución.
        
    """
    
    filename1, fs1 = sf.read(audioData_1)
    filename2, fs2 = sf.read(audioData_2)
    
    if len(filename1) > 500 and len(filename2) > 500:
        audioData_convol = fftconvolve(filename1, filename2)
    else:
        audioData_convol = np.convolve(filename1, filename2)
    
    return audioData_convol

