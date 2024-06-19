import numpy as np
import matplotlib.pyplot as plt

def secuencia_aleatoria():
   """
  Generates a random sequence of integers, plots it as a stem plot, and highlights the maximum and minimum values.

  This function creates a random sequence of 30 integers between 0 and 10 using NumPy's `randint` function.
  It then calculates the maximum and minimum values in the sequence and their corresponding indices.

  The function generates a plot using Matplotlib:
  - A stem plot is created to visualize the sequence.
  - Markers are added at the indices of the maximum and minimum values to highlight them.
  - Labels are added for the maximum and minimum values.
  - Axis labels are set for 'Muestra' (x-axis) and 'Amplitud' (y-axis).
  - A legend is added to identify the maximum and minimum markers.
  - The plot is displayed using `plt.show()`.

  The function does not return any value.

  Example usage:
  
  secuencia_aleatoria()
  """
   secuencia = np.random.randint(0,11,size=30)
   max_secuencia = max(secuencia)
   min_secuencia = min(secuencia)
   indice_max = np.where(secuencia == max_secuencia)
   indice_min = np.where(secuencia == min_secuencia)
   plt.title('Grafico de secuencia aleatoria entre 0 y 10')
   plt.stem(secuencia)
   plt.plot(indice_max,max_secuencia,"k*", label='Maximo')
   plt.plot(indice_min,min_secuencia,"y*", label='Minimo')
   plt.xlabel('Muestra')
   plt.ylabel('Amplitud')
   plt.legend()
   plt.show()
   plt.figure
    


if __name__ == '__main__':
   valor_max, valor_min, ind_max, ind_min = secuencia_aleatoria()
   print("los indices con el valor maximo (", valor_max, "), son: ", ind_max)
   print("los indices con el valor minimo (", valor_min, "), son: ", ind_min)