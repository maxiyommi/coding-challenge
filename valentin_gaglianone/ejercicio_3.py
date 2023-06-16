from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from ejercicio_2 import indicesmaximos, indicesminimos
import numpy as np


def carga(direccion):
    fs, data = read(direccion) 
    return fs, data

def promedio(data):
    
    promedio=sum(data)/len(data)
    
    return(promedio)

if __name__=="__main__":
    
    
    fs, data=carga("audio.wav")
    data = data[0]
    print(data)

    indicesminimos(data)
    indicesmaximos(data)
    duracion=10
    prom = promedio(data)
    print(prom)
    promedioprint=np.ones(duracion*fs)*prom
    plt.plot(np.arange(0,duracion,1/fs),data[0:duracion*fs])
    plt.plot(np.arange(0,duracion,1/fs),promedioprint)
    plt.show()
