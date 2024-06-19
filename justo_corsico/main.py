if __name__ == "__main__":
    import ejercicio_1 as e1
    import ejercicio_2 as e2
    import ejercicio_3 as e3
    import ejercicio_4 as e4
    from sympy.plotting import plot
    import numpy as np
    # ejercicio 1
    print('-'*50)
    print('EJERCICIO 1')
    print('-'*50)
    f_a_trozos = e1.generatePiecewiseFunc()
    e1.calcEnergiaPotencia(f_a_trozos)
    plot(f_a_trozos)

    # ejercicio 2
    print('-'*50)
    print('EJERCICIO 2')
    print('-'*50)
    secuencia_aleatoria = e2.secuencia_aleatoria()
    e2.plotarray(secuencia_aleatoria)

    # ejercicio 3
    print('-'*50)
    print('EJERCICIO 3')
    print('-'*50)
    print('Elija un archivo de audio para conocer su valor de amplitud promedio: ')
    print('-'*50)
    wavname = e3.cargar_wav()
    data, fs = e3.get_data(wavname)

    y_mean = np.mean(data)
    print('El promedio de todos los valores del vector es : ', y_mean)

    e3.plot_signal_and_average(data, fs, y_mean)

    # ejercicio 4
    print('-'*50)
    print('EJERCICIO 4')
    print('-'*50)
    print('Elija 2 archivos con formato wav para convolucionar: ')
    print('-'*50)
    audio_name1 = e3.cargar_wav()
    audio_data1, fs1 = e3.get_data(audio_name1)

    audio_name2 = e3.cargar_wav()
    audio_data2, fs2 = e3.get_data(audio_name2)

    audio_convolve = e4.get_convolve(audio_data1, audio_data2)

 

