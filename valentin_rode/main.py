from ejercicio_1 import *
from ejercicio_2 import *
from ejercicio_3 import *
from ejercicio_4 import *

if __name__=="__main__":
    #Ejercicio 1
    print("Ejercicio 1:")
    f=piecewise_function()
    energy_power(f)
    print("--------------------------------")
    #Ejercicio 2
    print("Ejercicio 2:")
    secuencia_aleatoria()
    print("--------------------------------")
    #Ejercicio 3
    print("Ejercicio 3:")
    ruta_archivo = "IR_Hall_example 3.wav"
    audio_array,sample_rate=cargar_audio(ruta_archivo)
    mean=max_min_mean(audio_array, sample_rate)
    get_plot(audio_array,sample_rate,mean)
    print("--------------------------------")
    #Ejercicio 4
    print("Ejercicio 4:")
    #Para probar np.convolve
    audio_data_1=np.array((5,4,3,2,5,6))
    audio_data_2=np.array((3,4,2,1,2))
    
    #Para probar fftconvolve
    #audio_data_1=np.linspace(0,1,501)
    #audio_data_2=np.linspace(0,1,500)
    convolve_audio(audio_data_1, audio_data_2)
    print("--------------------------------")