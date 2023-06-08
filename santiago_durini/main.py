if __name__ == "__main__":

    from ejercicio_1 import ej1, EyP
    from ejercicio_2 import ej2, grafico_2
    from ejercicio_3 import ej3, lectura, grafico_3
    from ejercicio_4 import ej4

    #Ejercicio 1:
    f = ej1()
    E, P = EyP(f)
    print('La energia de f(x) es:', E)
    print('La potencia promedio de f(x) es:', P)

    #Ejercicio 2:
    a, b, c = ej2()
    grafico_2(a,b,c)

    #Ejercicio 3:
    data, fs = lectura('Mono.wav')
    Max, Min, Promedio = ej3(data, fs)
    print('El valor maximo de la señal es:', Max)
    print('El valor minimo de la señal es:', Min)
    print('El valor promedio de la señal es:', Promedio)
    grafico_3(data, fs, Promedio)

    #Ejercicio 4:
    data1, fs1 = lectura('Sine_Sweep.wav')
    data2, fs2 = lectura('Filtro_Inverso.wav')
    convolucion = ej4(data1, data2)