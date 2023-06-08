import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import limit, integrate
from sympy import symbols, Piecewise
import soundfile as sf
import scipy




# Ejercicio 1

# Definición de la función
def f(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    elif 1 < x < 2:
        return 2 - x
    else:
        return 0

# Generación de valores de x en el rango deseado
x_values = np.linspace(-1, 3, 1000)

# Evaluación de la función en los valores de x
y_values = [f(x) for x in x_values]

# Graficar la función
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de la función f(x)')
plt.grid(True)
plt.show()

# Defino las variables t y T por medio de sympy para el cálculo de la energía y la potencia
t, T = sympy.symbols('t T')

# Para calcular la energía total es necesario definir simbólicamente la función f para poder utilizarla en E =  integrate(abs(f)**2,(t,-sympy.oo, sympy.oo))
x = symbols('x')
f = Piecewise((0, x <= 0), (x, (0 < x) & (x <= 1)), (2 - x, (1 < x) & (x < 2)), (0, x >= 2))
# Para la Energía Total:
energia_total_expr = abs(f)**2

# Utilizo la función evalf para evaluar expresión simbólica, sino el resulatdo arrojaba: Energía total: Integral(Abs(x)**2, (x, 0, 1)) + Integral(Abs(x - 2)**2, (x, 1, 2))
energia_total = integrate(energia_total_expr, (x, -sympy.oo, sympy.oo)).evalf()

print("Energía total:", energia_total)
# Para la Potencia Promedio:
P = limit((1/(2*T)*integrate(abs(f)**2,(x,-sympy.oo, sympy.oo))),T,sympy.oo)
print("Potencia promedio:", P)
# era de esperar que la Potencia Promedio sea 0 ya que la Energía Total





# Ejercicio 2

# Generar secuencia aleatoria de 30 elementos entre 0 y 10 por medio de np.random
secuencia = np.random.uniform(0, 10, size=30)
###### Intenté resolver los valores máximos y mínimos con el código a continuación, sin embargo me seguía arrojando un error

# max_random = max(secuencia)
# posicion_maximo = secuencia.index(max_random)
# print(posicion_maximo)

###### Decidí resolver con argmax() y argmin() de la librería Numpy

# Encontré el índice del valor máximo
indice_maximo = np.argmax(secuencia)

# Encontré el índice del valor mínimo
indice_minimo = np.argmin(secuencia)
print(secuencia)
print("Índice del valor máximo:", indice_maximo)
print("Índice del valor mínimo:", indice_minimo)
print("Recordar que las posiciones de ésta secuencias se comienzan a contar empezando con la posición 0 siendo el primer valor de la secuencia")
# Grafico la secuencia
plt.stem(secuencia)
plt.xlabel('Posición')
plt.ylabel('Valor de Amplitud')
plt.title('Gráfico de la Secuencia')
plt.grid(True)
plt.show()




# Ejercicio 3

# Usaré la librería sounfile
# Ruta al archivo de audio
ruta_archivo = 'Archivo_para_Parcial.wav'

# Cargar archivo de audio
audio, sr = sf.read(ruta_archivo)

# Leer metadatos
info = sf.info(ruta_archivo)

# Imprimir los metadatos
print("Metadatos del archivo de audio:")
print(info)
# Se obtienen los valores máximos y mínimos sobre la variable audio y se imprimen
valor_maximo = max(audio)
valor_minimo = min(audio)
print("El valor máximo del archivo es:", valor_maximo)
print("El valor mínimo del archivo es:", valor_minimo)

# Para el valor promedio de la señal utilizé la librería Numpy
valor_promedio = np.mean(audio)
print("Valor promedio de la señal:", valor_promedio)

##### Configuración para el eje x
rate = len(audio)
time = np.linspace(0, rate/sr, num=rate)
#####

# Grafico el valor promedio junto con la señal de audio en color rojo
plt.plot(time, audio,)
plt.axhline(valor_promedio, color='r')
plt.xlabel('Duración [s]')
plt.ylabel('Amplitud')
plt.title('Archivo para Parcial')
plt.grid(True)
plt.show()




# Ejercicio 4

# Si n cantidad de muestras de la señal es n>500, se aplicará  scipy.signal.fftconvolve, sino se aplicará numpy.convolve)
# Se leen los 2 archivos de audio por sound file. Para que se aplique scipy.signal.fftconvolve ambas señales deben contar con más de 500 muestras. Si tanto audio1 o audio2 tienen menos de 500 muetras, se aplicará numpy.convolve

def convolucion_audio(ruta_archivo1, ruta_archivo2):
    audio1, sr1 = sf.read(ruta_archivo1)
    audio2, sr2 = sf.read(ruta_archivo2)
    if sr1<500 or sr2<500:
        convolución = np.convolve(audio1, audio2)
    elif sr1>500 and sr2>500:
        convolución = scipy.signal.fftconvolve(audio1, audio2, mode='full', axes=None)
    return convolución

# Ejemplo con 2 archivos de audio

Conv1_2=convolucion_audio('Archivo_para_Parcial.wav','Archivo_para_parcial2.wav')

##### Configuración para el eje x
sr = 44100
rate12 = len(Conv1_2)
time12 = np.linspace(0, rate12/sr, num=rate12)
#####

# Se plotea el ejemplo
plt.plot(time12, Conv1_2)
plt.xlabel('Duración [s]')
plt.ylabel('Amplitud')
plt.title('Convolución')
plt.grid(True)
plt.show()