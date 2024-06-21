import numpy as np
from matplotlib import pyplot as plt

# Con la función random.rand genero 30 elementos con valores entre 0 y 1. Multiplicando por 10 a cada valor, el minimo es cero y el máximo 10
def secuencia_aleatoria():
    """
    Genera una secuencia aleatoria de 30 números con amplitud entre 0 y 10, encuentra y devuelve el índice del valor máximo de la secuencia.

    **Devuelve:**

    - `secuencia_aleatoria` (numpy.ndarray): Un vector NumPy que contiene la secuencia de 30 números aleatorios generada.

    **Ejemplo de uso:**

    ```python
    secuencia_aleatoria_resultado = secuencia_aleatoria()
    print(f'Secuencia aleatoria: {secuencia_aleatoria_resultado}')
    ```

    **Explicación del código:**

    1. **Generar secuencia aleatoria:**
        - Se utiliza la función `np.random.rand(30)` de NumPy para generar un vector de 30 números aleatorios entre 0 y 1.
        - Se multiplica el vector por 10 para ajustar la amplitud de los números entre 0 y 10.
        - Se asigna el vector a la variable `secuencia_aleatoria`.

    2. **Mostrar secuencia aleatoria:**
        - Se utiliza la función `print()` para mostrar un mensaje informativo junto con la secuencia aleatoria completa.

    3. **Encontrar índice del valor máximo:**
        - Se utiliza la función `np.argmax()` de NumPy para encontrar el índice del valor máximo dentro del vector `secuencia_aleatoria`.
        - El índice representa la posición del elemento con el valor más alto en la secuencia.

    4. **Mostrar índice del valor máximo:**
        - Se utiliza la función `print()` para mostrar un mensaje informativo junto con el índice del valor máximo encontrado.

    5. **Devolver secuencia aleatoria:**
        - Se devuelve el vector `secuencia_aleatoria` que contiene la secuencia de 30 números aleatorios generada.

    **Notas importantes:**

    - La función no modifica la secuencia aleatoria original.
    - El índice del valor máximo puede variar en cada ejecución de la función debido a la naturaleza aleatoria de la generación de números.
    """
    secuencia_aleatoria = np.random.rand(30) * 10

    print('Secuencia de 30 números aleatorios con amplitud entre 0 y 10 :', secuencia_aleatoria)

    indice = np.argmax(secuencia_aleatoria)

    print('El índice del valor máximo es: ', indice)
    return(secuencia_aleatoria)

def plotarray(a):
    """
    Genera un gráfico de una secuencia aleatoria de valores con marcadores para el valor máximo y mínimo resaltados.

    **Argumentos:**

    - `a` (numpy.ndarray): Un vector NumPy que contiene la secuencia de valores a graficar.

    **Retorno:**

    No se devuelve ningún valor, pero la función muestra el gráfico de la secuencia aleatoria con los valores máximo y mínimo resaltados.

    **Ejemplo de uso:**

    ```python
    secuencia_aleatoria = secuencia_aleatoria()  # Suponiendo que tienes una función 'secuencia_aleatoria'
    plotarray(secuencia_aleatoria)
    ```

    **Explicación del código:**

    1. **Generar un arreglo de tiempo:**
        - Se crea un arreglo de tiempo `t` utilizando `np.linspace` para representar el eje horizontal del gráfico con 30 valores espaciados uniformemente entre 0 y 29.

    2. **Crear un gráfico de tallo:**
        - Se utiliza `plt.stem(t, a)` para generar un gráfico de tallo que representa la secuencia de valores en `a`.

    3. **Configurar el gráfico:**
        - Se establecen las etiquetas de los ejes x e y mediante `plt.xlabel` y `plt.ylabel`.
        - Se activa la cuadrícula del gráfico con `plt.grid()`.
        - Se agrega un título descriptivo con `plt.title`.

    4. **Encontrar valores máximo y mínimo:**
        - Se utilizan `max(a)` y `min(a)` para encontrar el valor máximo y mínimo dentro del vector `a`.

    5. **Encontrar índices del máximo y mínimo:**
        - Se utiliza `np.argmax(a)` para encontrar el índice del valor máximo en `a`.
        - Se utiliza `np.argmin(a)` para encontrar el índice del valor mínimo en `a`.

    6. **Crear etiquetas personalizadas:**
        - Se define una lista `custom_labels` con etiquetas para los marcadores del máximo y mínimo.

    7. **Graficar valores máximo y mínimo resaltados:**
        - Se utiliza `plt.scatter` para graficar círculos naranjas y rojos en las posiciones del máximo y mínimo (`max_index`, `max_value`) y (`min_index`, `min_value`), respectivamente.
        - Se personaliza el tamaño (s=200) y las etiquetas de los marcadores utilizando `label=custom_labels`.

    8. **Agregar leyenda:**
        - Se utiliza `plt.legend(loc='upper left')` para crear una leyenda que explique los marcadores del máximo y mínimo.

    9. **Mostrar el gráfico:**
        - Se utiliza `plt.show()` para mostrar el gráfico generado.
    """
    t = np.linspace(0, 29, 30)
    plt.stem(t, a)
    plt.xlabel('Indice')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.title('Secuencia aleatoria de valores')
    max_value = max(a)
    min_value = min(a)
    max_index = np.argmax(a)
    min_index = np.argmin(a)
    custom_labels = ['Máximo (Naranja)', 'Mínimo (Rojo)']
    plt.scatter(max_index, max_value, marker='o', s=200, color='orange', label=custom_labels[0])
    plt.scatter(min_index, min_value, marker='o', s=200, color='red', label=custom_labels[1])
    plt.legend(loc='upper left')
    plt.show()

