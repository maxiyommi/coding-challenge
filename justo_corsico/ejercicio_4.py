import numpy as np
import soundfile as sf
from ejercicio_3 import cargar_wav
import scipy


def get_convolve(audio_data1, audio_data2):
    """
    Calcula y devuelve la convolución discreta de dos señales de audio utilizando la transformada rápida de Fourier (FFT).

    **Argumentos:**

    - `audio_data1` (numpy.ndarray): Un arreglo NumPy que representa la primera señal de audio.
    - `audio_data2` (numpy.ndarray): Un arreglo NumPy que representa la segunda señal de audio. Ambos arreglos deben tener la misma longitud o tamaños compatibles para la convolución.

    **Devuelve:**

    - `conv` (numpy.ndarray): Un arreglo NumPy que contiene la convolución de las señales de audio `audio_data1` y `audio_data2`. El tamaño de la salida depende del modo de convolución utilizado (en este caso, 'same').

    **Ejemplo de uso:**

    ```python
    # Suponiendo que audio_data1 y audio_data2 son arreglos NumPy de audio
    convoluted_audio = get_convolve(audio_data1, audio_data2)
    # Puede procesar o reproducir el audio convolucionado (convoluted_audio)
    ```

    **Explicación:**

    1. **Convolución FFT:**
        - La función utiliza `scipy.signal.fftconvolve` para calcular la convolución de las señales de audio `audio_data1` y `audio_data2` utilizando la transformada rápida de Fourier (FFT).
        - La FFT es un método eficiente para calcular convoluciones de señales grandes.
        - El modo de convolución se establece en 'same' para que la salida tenga la misma longitud que la señal de entrada más corta.

    2. **Imprimir y devolver la convolución:**
        - Se imprime la convolución calculada usando `print(conv)` para fines informativos (opcional).
        - La función devuelve el arreglo `conv` que contiene la convolución de las señales de audio.
    """
    conv = scipy.signal.fftconvolve(audio_data1, audio_data2, mode='same')
    print(conv)
    return conv 

