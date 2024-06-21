import numpy as np
import scipy.signal as sp
import soundfile as sf
import matplotlib.pyplot as plt

def Convolucion(Audio1, Audio2):
    """
    Performs convolution between two audio signals, choosing the appropriate method based on sample size.

    Args:
    Audio1 (str): Path to the first audio file.
    Audio2 (str): Path to the second audio file.

    Returns:
    np.ndarray: The convolved audio signal as a NumPy array.
    """
    
    Audio1, fs1 = sf.read(Audio1)
    Audio2, fs2 = sf.read(Audio2)

    if fs1==fs2:
        if fs1>= 500:
            impulso = sp.fftconvolve(Audio1, Audio2,"same") # Realiza la convolución con el método de la transformada rápida de Fourier
        elif 0< fs1 <=500:
            impulso = np.convolve(Audio1, Audio2)
        else:
            print("No tiene cantidad de muestras")    
    else:
        print("Audios con distintas cantidad de muestras")

    impulso /= max(abs(impulso))
    sf.write("output.wav", impulso, fs1)

    return impulso

def plotcon(audioData_convol):
    """
    Plots the convolved audio signal from the provided data array.

    Parameters:
    - audioData_convol (numpy.ndarray): A NumPy array containing the convolved audio data.

    Raises:
    - FileNotFoundError: If the "output.wav" file is not found.

    Returns:
    - None

    Plots the convolved audio signal from the provided `audioData_convol` array. 
    This function assumes the data represents samples over time. It generates a time 
    axis based on the data length and sampling rate (assumed to be available 
    from elsewhere). The plot includes a title, axis labels, and is displayed using 
    Matplotlib.
    """
    # Read the saved WAV file for plotting
    info, fs = sf.read("output.wav")

    t = np.linspace(0, len(audioData_convol) / fs, len(audioData_convol))
    plt.plot(t, audioData_convol)
    plt.title("convolucion", size=16)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.show()

if __name__=="__main__":
    
    audioData_convol = Convolucion("Challenge/Sine_Sweep.wav", "Challenge/Filtro_Inverso.wav")

    plotcon(audioData_convol)