import wave
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from IPython.display import clear_output

clear_output()
root = Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
file = filedialog.askopenfilename(filetypes=[("wav files", "*.wav")])

with wave.open(file, 'rb') as wf:
    fs = wf.getframerate()
    nSamples = wf.getnframes()
    duration = nSamples / fs
    nChannels = wf.getnchannels()
    audioData = wf.readframes(nSamples)
    sampwidth = wf.getsampwidth()
    bitDepth = sampwidth * 8
    if bitDepth != 16:
        WAV = wavfile.read(file)
        signal = WAV[1]
        time = np.linspace(0, len(signal) / WAV[0], len(signal))
        signal = signal / np.max(np.abs(signal))
    else:
        signal = np.frombuffer(audioData, dtype=np.int16)
        signal = signal[0::2] if nChannels == 2 else signal
        signal = signal / np.max(np.abs(signal))
        time = np.linspace(0, duration, num=nSamples)

    print("La frecuencia de sampleo: ", fs)
    print("La cantidad de muestras: ", nSamples)
    print("La duración: ", duration)
    print("La cantidad de canales: ", nChannels)
    print("La profundidad de bits:", bitDepth)
    print("Valor máximo de la señal:", np.max(signal))
    print("Valor mínimo de la señal:", np.min(signal))
    print("Promedio de la señal:", np.mean(signal))

    plt.figure(figsize=(12, 6))
    plt.plot(time, signal, color='b', label='Señal de Audio')
    plt.axhline(y=np.mean(signal), color='r', linestyle='--', label=f'Promedio ({np.mean(signal):.2f})')

    plt.title('Señal de Audio y Valor Promedio')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud Normalizada')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
