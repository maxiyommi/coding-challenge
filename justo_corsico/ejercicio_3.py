import numpy as np
import soundfile as sf
from tkinter import Tk, filedialog
from ipywidgets import Button
from IPython.display import clear_output, display
from matplotlib import pyplot as plt
def cargar_wav():
    """
    Allows the user to load WAV files.

    return: A list with the files path.
    """
    
    def select_file():
        clear_output()
        root = Tk()
        root.withdraw() # Hide the main window.
        root.call('wm', 'attributes', '.', '-topmost', True) # Raise the root to the top of all windows.
        wavname = (filedialog.askopenfilename()) # List of selected files will be set button's file attribute.
        print(wavname) # Print the list of files selected.
        return wavname

    fileselect = Button(description="Seleccione el archivo")
    fileselect.on_click(select_file)
    wavname = select_file()
    return wavname
def get_data(archivo_wav):
    """
    Vectoriza un archivo wav
    Parametros:
        archivo_wav(WAV): nombre del archivo wav
    Return: 
        data(np_array):Array con los valores de amplitud  
        fs(int): frecuencia de muestreo del archivo
    """  
    data,fs=sf.read(archivo_wav)
    return data,fs

def plot_signal_and_average(signal, sample_rate, average_value):
    """
    Plots a signal (NumPy array) and its average value with different colors and a legend.

    Args:
        signal (np.ndarray): The signal data as a NumPy array.
        average_value (float): The average value of the signal.

    Returns:
        None
    """


    duracion=(len(signal)/sample_rate)
    t=np.linspace(0,duracion,len(signal))


    plt.plot(t, signal, label='Señal', color='blue')


    plt.axhline(y=average_value, color='red', linestyle='--', label='Promedio')


    plt.xlabel('Tiempo (muestras)')
    plt.ylabel('Amplitud')
    plt.title('Señal y valor promedio')


    plt.legend()


    plt.show()



