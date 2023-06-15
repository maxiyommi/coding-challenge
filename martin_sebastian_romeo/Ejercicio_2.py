import numpy as np
import matplotlib.pyplot as plt
# importo librerias


def Fun_2 ():
    """
    La funcion genera un array de 30 numeros aleatorios entre 0 y 10.
    Luego crea dos array correspondientes a los indices de los valores maximos y minimos de la secuencia
    Grafica la secuencia, resaltando los maximos y los minimos.
    
    """
    
    
    #Genero la secuencia de 30 numeros aleatorios enteros entre 0 y 10
    num = np.random.randint(0, 10, 30)
    
    #Genero los array con los indices de los valores maximos y minimos
    indices_max = np.where(num == np.max(num))[0]
    indices_min = np.where(num == np.min(num))[0]
    
    #Grafico
    fig = plt.figure()
    plt.stem(num)
    plt.xticks(range(0,31,2)) #Defino el paso del eje x
    plt.yticks(range(0,11)) #Defino el paso del eje y
    plt.title("secuencia")
    plt.plot(indices_max, num[indices_max], 'y*', markersize=12, label='Máximo') #Le agrego un marcador a los maximos
    plt.plot(indices_min, num[indices_min], 'k*', markersize=12, label='Mínimo') #Le agrego un marcador a los minimos
    plt.legend(loc = "best") #Agrego la leyenda, haciendo que elija la mejor posicion donde ubicarse
    plt.xlabel("rango")
    plt.ylabel("amplitud")
    return()

