import numpy as np
import matplotlib.pyplot as plt
def secuencia_aleatoria():
    sec = np.random.randint(0,10,30) 
    indice_maximo = np.argmax(sec)
    indice_minimo = np.argmin(sec)
    valor_maximo = sec[indice_maximo]
    valor_minimo = sec[indice_minimo]

    # Gráfico
    plt.plot(sec, label="Secuencia aleatoria")
    plt.scatter(indice_maximo, valor_maximo, color="Orange", label="Máximo")
    plt.scatter(indice_minimo, valor_minimo, color="green", label="Mínimo")
    # Labels
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.title("Secuencia aleatoria")
    plt.legend()
    # Se muestra la gráfica
    plt.show()
if __name__ == '__main__':
    secuencia_aleatoria()