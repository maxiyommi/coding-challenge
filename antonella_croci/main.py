from ejercicio_1 import funcion
from ejercicio_1 import graficar
from ejercicio_1 import energia_potencia
from ejercicio_2 import secuencia
from ejercicio_2 import max_y_min
from ejercicio_2 import graficar2
from ejercicio_3 import cargar
from ejercicio_3 import max_min_audio
from ejercicio_3 import mean
from ejercicio_3 import grafico3
from ejercicio_4 import convolve
from sympy.interactive import printing
printing.init_printing(use_latex="mathjax")
from IPython.display import display

def main(archivo1, archivo2, archivo3):
    """
    Archivo final para el parcial.

    """
    # Ejercicio 1
    print("EJERCICIO 1")

    # Expresar de manera simbólica la función 

    x, fx = funcion()
    display(fx)

    # Graficar la expresión simbólica

    graficar(fx)

    # Calcular la energía y potencia de la función

    energia, potencia = energia_potencia(x, fx)

    print("La enegía de la función es:", energia)
    print("La potencia de la función es:", potencia)

    # Ejercicio 2
    print("EJERCICIO 2")
    # Generar una secuencia aleatoria de 30 elementos, con amplitud de 0 a 10

    lista = secuencia()

    print("La lista generada es:", lista)

    # Encontrar los índices correspondientes a los valores máximos y mínimos de la secuencia.

    min, indices_min, max, indices_max = max_y_min(lista)

    print("El valor mínimo de la lista es: ", min)
    print("Posiciones del valor mínimo:", indices_min)
    print("El valor máximo de la lista es: ", max)
    print("Posiciones del valor máximo", indices_max)

    # Graficar la secuencia obtenida, con los máximos y mínimos

    graficar2(lista,min,max,indices_min,indices_max)

    # Ejercicio 3
    print("EJERCICIO 3")
    # Cargar un archivo de audio para extraer su información

    data, fs = cargar(archivo1)

    # Obtener los valores máximos y mínimos del archivo de audio

    max, min = max_min_audio(data)
    
    print("El valor máximo del archivo de audio es:", max)
    print("El valor mínimo del archivo de audio es:", min)

    # Obtener el valor promedio del archivo de audio

    promedio = mean(data)
    print("El promedio de la señal de audio es:", promedio)
    
    # Grafica la señal de audio junto con su valor promedio

    grafico3(data, fs, promedio)

    # Ejercicio 4 
    print("EJERCICIO 4")

    # Lectura de los dos archivos de audio 

    data1, fs1 = cargar(archivo2)
    data2, fs2 = cargar(archivo3)
    
    # Convolucionar dos señales de audio

    conv = convolve(data1, data2)
    


if __name__ == "__main__":
    main("IR1.wav","Filtro_Inverso.wav","Sine_Sweep.wav")

