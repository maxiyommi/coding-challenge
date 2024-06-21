from numpy import convolve
from scipy.signal import fftconvolve
import soundfile as sf

def convolucion(audioData_1,audioData_2):
    """
  Performs convolution of two audio data sequences.

  This function takes two NumPy arrays, `audioData_1` and `audioData_2`, representing audio data sequences,
  and returns their convolution. The convolution method is chosen based on the lengths of the input sequences:

  - If the length of either `audioData_1` or `audioData_2` is greater than or equal to 500, the function
    utilizes the `fftconvolve` (fast Fourier transform convolution) function from NumPy for efficiency.
  - If both sequences are shorter than 500 elements, the standard `convolve` function from NumPy is used
    for simpler calculations.

  Args:
      audioData_1 (numpy.ndarray): The first audio data sequence as a NumPy array.
      audioData_2 (numpy.ndarray): The second audio data sequence as a NumPy array.

  Returns:
      numpy.ndarray: The convolution of the two audio data sequences.

  Raises:
      ValueError: If either `audioData_1` or `audioData_2` is not a NumPy array.
  """
    if len(audioData_1) & len(audioData_2) >= 500:
        audio_convolve = fftconvolve(audioData_1,audioData_2)
    else:
        audio_convolve = convolve(audioData_1,audioData_2)
    return audio_convolve

if __name__ == '__main__':
    data1, fs = sf.read('sine-sweep.wav')
    data2, fs = sf.read('inverse-filter.wav')
    datafinal = convolucion(data1,data2)
    print('La convolucion es: ',datafinal)