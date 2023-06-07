from ejercicio_1 import *
from ejercicio_2 import *
from ejercicio_3 import *
from ejercicio_4 import *
from tkinter import *
import sounddevice as sd

if __name__ == "__main__":
    def ejer_1():
        # 1- Expresar la función de manera simbólica.
        x = sym.Symbol('x')
        f1 = 0
        f2 = x
        f3 = 2-x
        f4 = 0
        f = sym.Piecewise((f1, x<=0),(f2, (x>0)&(x<=1)),(f3, (x>1)&(x<2)),(f4, x>=2))   # Defino la función a trozos
        T = sym.Symbol('T')
        E =  integrate(abs(f)**2,(x,-sym.oo, sym.oo))   # Energía de la señal
        P = limit((1/(2*T)*integrate(abs(f)**2,(x,-sym.oo, sym.oo))),T,sym.oo)  # Potencia de la señal
        # 2- Graficar la expresión simbólica.
        plot(f, title="Función a trozos")
        # 3- Calcular (si existe) el valor numérico de la energía total y potencia promedio de la función.
        print(E.evalf())
        print(P.evalf())

    def ejer_2():
        # 1
        print(array)
        # 2
        print(max_index, min_index)
        # 3- Graficar la secuencia con los máximos y mínimos en un mismo gráfico, indicando con leyendas y etiquetas que representan.
        data = array    
        grafico_min_max(data)

    def ejer_3():
        # 1
        audioFileName = "luca-falchini\clarinete.wav"
        fs, audiodata = read_wav(audioFileName)
        print('AudioFile = {}, Sample Rate = {} [Samples/Sec], Wav format = {}, Samples = {}, length = {}'.format(audioFileName,fs,audiodata.dtype,audiodata.shape[0],audiodata.shape[0]/fs))
        # 2
        max_val, min_val = min_max(audiodata)
        print(max_val, min_val)   
        # 3     
        grafico_min_max_mean(audiodata, fs)
    fs, audio1 = read_wav('luca-falchini/clarinete.wav')
    fs2, audio2 = read_wav('luca-falchini/Mono.wav')
    audio_conv = convolucion(audio1, audio2)
    def ejer_4():        
        grafico_min_max_mean(audio_conv, fs2, "Convolución")
    
    def reproducir1():
        '''Función para reproducir audio 1'''
        sd.play(audio1, fs)
    def reproducir2():
        '''Función para reproducir audio 2'''
        sd.play(audio2, fs2)
    def reproducir3():
        '''Función para reproducir convolución entre audio 1 y audio 2'''
        sd.play(audio_conv, fs)
        
    def parar():
        '''Función para parar audio'''
        sd.stop()
    
    
    window = Tk()
    window.title("Coding Challenge - Python (Junio-2023) - Luca Falchini")
    
    button = Button(window,text="Ejercicio_1",command=ejer_1,font=("Arial", 16),fg="blue")
    button2 = Button(window,text="Ejercicio_2",command=ejer_2,font=("Arial", 16),fg="blue")
    button3 = Button(window,text="Ejercicio_3",command=ejer_3,font=("Arial", 16),fg="blue")
    button4 = Button(window,text="Ejercicio_4",command=ejer_4,font=("Arial", 16),fg="blue")
    button5 = Button(window,text="Reproducir Audio 1",command=reproducir1,font=("Arial", 16),fg="blue")
    button6 = Button(window,text="Reproducir Audio 2",command=reproducir2,font=("Arial", 16),fg="blue")
    button7 = Button(window,text="Reproducir Convolución",command=reproducir3,font=("Arial", 16),fg="blue")
    button8 = Button(window,text="Parar reproducción",command=parar,font=("Arial", 16),fg="blue")
    
    button.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=2, column=0)
    button6.grid(row=2, column=1)
    button7.grid(row=2, column=2)
    button8.grid(row=3, column=1)

    window.mainloop()
