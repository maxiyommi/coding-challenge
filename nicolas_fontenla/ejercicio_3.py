import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def lectura_audio(file):
    """
    Reads an audio file and returns the signal data and sampling frequency.

    This function takes the path to an audio file (`file`) as input and reads the audio data using the `soundfile` library.
    It returns the audio signal data (`data`) as a NumPy array and the sampling frequency (`fs`) as an integer.

    Args:
        file (str): Path to the audio file.

    Returns:
        tuple: A tuple containing the audio signal data (`data`) and the sampling frequency (`fs`).

    Raises:
        FileNotFoundError: If the specified audio file cannot be found.
        SoundfileError: If an error occurs during audio file reading using `soundfile`.
    """
    data, fs = sf.read(file)
    return data, fs

def max_min_prom(data, fs):
    """
    Calculates the maximum, minimum, and average values of an audio signal and generates a plot.

    This function takes an audio signal data (`data`) and its sampling frequency (`fs`) as input.
    It calculates the maximum value (`maximo`), minimum value (`minimo`), and average value (`promedio`) of the signal.
    It also calls the `grafico_ej3` function to generate a plot of the signal and its average value.

    Args:
        data (numpy.ndarray): Audio signal data as a NumPy array.
        fs (int): Sampling frequency in Hz.

    Returns:
        tuple: A tuple containing the maximum value (`maximo`), minimum value (`minimo`), and average value (`promedio`) of the signal.
    """

    maximo = max(data)
    minimo = min(data)
    promedio = np.mean(data)
    grafico_ej3(data, promedio,fs) 
    return maximo, minimo, promedio

def grafico_ej3(data, promedio,fs):
    """
    Generates a plot of an audio signal and its average value.

    This function takes an audio signal data (`data`), its average value (`promedio`), and its sampling frequency (`fs`) as input.
    It creates a time axis (`t`) based on the signal length and sampling frequency.
    It generates a plot with the following elements:
        - Signal plot: A line plot of the original audio signal.
        - Average value line: A horizontal dashed line at the value of the average signal.
        - Labels: Labels for the x-axis ("Tiempo [s]") and y-axis ("Amplitud").
        - Legend: A legend indicating the "Señal" and "Valor promedio" lines.
        - Title: A title "Grafico de la señal y su promedio".

    The plot is displayed using `matplotlib.pyplot.show()`.
    """
    t = np.linspace(0, data.shape[0]/fs, data.shape[0])
    plt.title("Grafico de la señal y su promedio")
    plt.plot(t,data,label="Señal")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.axhline(y=promedio, color='r', linestyle='--', label="Valor promedio")
    plt.legend()
    plt.show()
    plt.figure()
    
if __name__ == "__main__":
    valor_max, valor_min, prom = lectura_audio("sine-sweep.wav")   
    print("El valor máximo es: ", valor_max)
    print("El valor minimo es: ", valor_min)
    print("El valor promedio es: ",prom)