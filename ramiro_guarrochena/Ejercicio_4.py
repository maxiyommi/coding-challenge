import soundfile as sf
import numpy as np
import scipy.signal as signal

def cargar_audios(ruta1, ruta2):
    try:
        # Cargar las señales de audio y las frecuencias de muestreo
        audioData_1, fs1 = sf.read(ruta1)
        audioData_2, fs2 = sf.read(ruta2)
        
        # Verificar la longitud de las señales de audio
        if len(audioData_1) > 500 and len(audioData_2) > 500:
            # Usar scipy.signal.fftconvolve para señales largas
            audioData_convol = signal.fftconvolve(audioData_1, audioData_2, mode='full')
        else:
            # Usar numpy.convolve para señales cortas o moderadas
            audioData_convol = np.convolve(audioData_1, audioData_2, mode='full')
        
        return audioData_convol
    
    except Exception as e:
        print("Error al cargar o convolucionar los audios:", e)
        return None

# Ejemplo de uso:
if __name__ == "__main__":
    ruta_audio_1 = r"C:\Users\ramag\Desktop\Grabacion II\TP1\Archivos multipista\01_Kick.wav"
    ruta_audio_2 = r"C:\Users\ramag\Desktop\Grabacion II\TP1\Archivos multipista\12_Violin1.wav"
    
    resultado_convolucion = cargar_audios(ruta_audio_1, ruta_audio_2)
    
