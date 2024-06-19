from Ejercicio_1 import Energia_Potencia, funcion
from Ejercicio_2 import Numeros, plot_Num
from Ejercicio_3 import ValoresWav, plotValWav
from Ejercicio_4 import Convolucion, plotcon

f,x = funcion()

E,P = Energia_Potencia(f,x)

# Mostrar los resultados
print(f'Energía total: {E.evalf()}')
print(f'Potencia promedio: {P.evalf()}')

secuencia, indice_max, indice_min= Numeros(0,10,30)

plot_Num(secuencia,indice_max,indice_min)

valor_max,valor_min,valor_promedio,duracion,y = ValoresWav("Challenge/IR1.wav")

# Mostrar metadata
print(f'Duración del audio: {duracion} segundos')
print(f'Valor máximo: {valor_max}')
print(f'Valor mínimo: {valor_min}')
print(f'Valor promedio: {valor_promedio}')

plotValWav(valor_max,valor_min,valor_promedio,duracion,y)

audioData_convol = Convolucion("Challenge/Sine_Sweep.wav", "Challenge/Filtro_Inverso.wav")

plotcon(audioData_convol)

