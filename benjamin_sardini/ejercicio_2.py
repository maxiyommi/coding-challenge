import numpy as np
import matplotlib.pyplot as plt

def aleatorios(indice_0, indice_final, cantidad_valores):
    """
    La función se encarga de armar una secuencia de 30 numeros aleatorios entre el uno y el diez, para luego graficarla de forma discreta señalando sus valores máximos y mínimos.
    Parámetros:
        indice_0: entero que determinará el minimo valor que podrá tomar un numero aleatorio.
        indice_final: entero que determinará el máximo valor que podrá tomar un numero aleatorio.
        cantidad_valores: cantidad de numeros aleatorios a generar
    Returns:
        -
    """
    
    secuencia = np.random.randint(indice_0, indice_final, cantidad_valores+1)

    maximo = np.argmax(secuencia)
    minimo = np.argmin(secuencia)

    eje_x = np.arange(len(secuencia))

    plt.stem(eje_x,secuencia)
    #plt.plot(eje_x, secuencia, label='Secuencia')
    plt.plot(maximo, secuencia[maximo], marker='o',color='red', label='Máximo')
    plt.plot(minimo, secuencia[minimo], marker='o', color='green', label='Mínimo')
    plt.xlabel('Eje X')
    plt.ylabel('Valor')
    plt.title('Secuencia Aleatoria con Máximo y Mínimo')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':

    aleatorios(0, 10, 30)
