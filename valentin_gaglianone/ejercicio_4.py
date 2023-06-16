
if __name__=="__main__":
    from scipy.signal import fftconvolve
    import numpy as np
    from scipy.io.wavfile import read
    import matplotlib.pyplot as plt
 
def convolucion(audioData_1,audioData_2):
    if len(audioData_1)>500 or len(audioData_2)>500:
        if len(audioData_2)>len(audioData_1):
            audioData_1=np.pad(audioData_1,len(audioData_2)-len(audioData_1))
        else:
            audioData_2=np.pad(audioData_1,len(audioData_1)-len(audioData_2))
        convolucion=np.convolve(audioData_1,audioData_2)
    else: convolucion=fftconvolve(audioData_1, audioData_2, mode='full', axes=None)
    return convolucion       
if __name__=="__main__":
    fs1, audioData_1= read("audio1.wav")
    fs2, audioData_2= read("audio2.wav")
    tiempo=np.arange(0,1,1/44100)
    Resultados=convolucion(audioData_1,audioData_2)
    convol1seg=Resultados[0:44100]
    plt.plot(tiempo,convol1seg)
    plt.show()
