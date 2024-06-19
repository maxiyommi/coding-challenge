import numpy as np
import scipy.signal as sp

def convolve_audio(audioData_1, audioData_2):
    """
    Convolves two audio signals using the specified method.

    Arguments:
        audioData_1 (ndarray): NumPy array containing the amplitude values of audio signal 1.
        audioData_2 (ndarray): NumPy array containing the amplitude values of audio signal 2.

    Returns:
        ndarray: NumPy array containing the amplitude values of the convolved signal.
    """

    if len(audioData_1) > 500 or len(audioData_2) > 500:
        print("Usando FFT convolve")
        audioData_convol = sp.fftconvolve(audioData_1, audioData_2)
        print(audioData_convol[0:10])
    else:
        print("Usando np convolve")
        audioData_convol = np.convolve(audioData_1, audioData_2)
        print(audioData_convol[0:10])
    return audioData_convol
if __name__ == '__main__':
    #Para probar np.convolve
    #audio_data_1=np.array((5,4,3,2,5,6))
    #audio_data_2=np.array((3,4,2,1,2))

    #Para probar fftconvolve
    audio_data_1=np.linspace(0,1,501)
    audio_data_2=np.linspace(0,1,500)

    convolve_audio(audio_data_1,audio_data_2)