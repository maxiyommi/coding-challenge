import numpy as np
import matplotlib.pyplot as plt

# 1- Generar una secuencia aleatoria de 30 elementos, con amplitud entre 0 y 10.
array = np.random.random(size=30)*10

# 2- Encontrar los índices correspondientes a los valores máximos y mínimos de la secuencia
max_index = np.argmax(array)
min_index = np.argmin(array)

def grafico_min_max(data, graph_name= " Mínimo y máximo"):
    """
    Función que grafica un conjunto de datos de un array y muestra su máximo y mínimo.
    
    Parámetros
    ----------
    data: array
        array de datos

    graph_name: str
        nombre del gráfico

    Returns
    -------
    Gráfico con el máximo y el mínimo.
    """
    max_ind = np.argmax(data)
    min_ind = np.argmin(data)
    n = np.arange(0,len(data))    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.annotate("Máximo (x;y):({};{})".format(max_ind,np.round(np.max(data),2)),
                xy=(max_ind, np.max(data)), xycoords='data',
                xytext=(max_ind+1, np.max(data)+1), textcoords='data',
                size=10, va="center", ha="center",
                bbox=dict(boxstyle="round4", fc="w"),
                arrowprops=dict(arrowstyle="-|>",connectionstyle="arc3,rad=-0.2", fc="w"))  # Indico el máximo valor
    ax.annotate("Mínimo (x;y):({};{})".format(min_ind,np.round(np.min(data),2)),
                xy=(min_ind, np.min(data)), xycoords='data',
                xytext=(min_ind+1, np.min(data)+1), textcoords='data',
                size=10, va="center", ha="center",
                bbox=dict(boxstyle="round4", fc="w"),
                arrowprops=dict(arrowstyle="-|>",connectionstyle="arc3,rad=-0.2", fc="w"))  # indico el mínimo valor
    ax.stem(n,data) 
    ax.grid()
    ax.set_xlim(-0.5,len(data)+1)
    ax.set_ylim(-0.5,np.max(data)+1)
    ax.set_xlabel("Muestras")
    ax.set_ylabel("Amplitud")
    plt.title(graph_name)
    plt.show()

if __name__ == "__main__":
    # 1
    print(array)
    # 2
    print(max_index, min_index)
    
    # 3- Graficar la secuencia con los máximos y mínimos en un mismo gráfico, indicando con leyendas y etiquetas que representan.
    data = array    
    grafico_min_max(data)