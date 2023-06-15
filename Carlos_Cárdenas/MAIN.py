from EJRC_1 import eyp_señal
from graficar_func import graficar_func

print("Ejercicio 1:")
x, f = eyp_señal(0, 1, 2)
graficar_func(x, f)
print("\n")

from EJRC_2 import secuencia
from graficar_sec import graficar_sec

print("Ejercicio 2:")
sec, m, mi, ima, imi = secuencia(10, 31)
graficar_sec(sec, m, mi, ima, imi)
print("\n")

from EJRC_3 import audio
from graficar_vm import graficar_vm

print("Ejercicio 3:")
au = audio("sine_sweep.wav")
graficar_vm(au)
print("\n")

from EJRC_4 import convolucion
from grafico_señal import grafico

print("Ejercicio 4:")
conv = convolucion("filtro_inverso.wav", "ruido_rosa.wav")
grafico(conv)
print("El array de la convolución puede ser visualizado en el explorador de variables con el nombre 'conv' y el archivo de audio generado se encuentra en la carpeta del proyecto.")

