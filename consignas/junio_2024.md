# Coding Challenge - Python (Junio-2024)

<center><img src="https://raw.githubusercontent.com/maxiyommi/signal-systems/master/LogoPractica.png" width="300"/></center>

## Consigna

A continuación se presentan varios puntos que deben ser completados en distintos archivos .py, con el siguiente formato: <ejercicio_numero>.py (Ej: ejercicio_1.py). Todos los ejercicios deben ser llamados desde un main.py de manera secuencial. Se podrá reutilizar las funciones, la cantidad de veces necesarias.

* Todas las funciones deben contar con su docstring (descripción, argumentos de entrada, argumentos de salida, entre otros).
* Todos los gráficos deben tener correctamente etiquetados los ejes.
* Todas las señales, archivos o elementos necesarios para reproducir la respuesta deben ser enviados.

> Solicitamos utilizar en lo posible las librerías y métodos visto en clase.

## Ejercicio_1
Dada la siguiente función continua:

![](ejercicio_1.png)
<!---
$$ f(x)=\begin{cases} 
0, \text{ para } x<=0 \\  
x, \text{  para } 0<x<=1 \\
2-(x), \text{ para } 1<x<2 \\ 
0, \text{ para } x>=2 \\  
\end{cases}$$
-->
1. Expresar la función de manera simbólica.
2. Graficar la expresión simbólica.
3. Calcular (si existe) el valor numérico de la energía total y potencia promedio de la función. 

## Ejercicio_2
Utilizando Numpy,
1. Generar una secuencia aleatoria de 30 elementos, con amplitud entre 0 y 10.
2. Encontrar los índices correspondientes a los valores máximos y mínimos de la secuencia
3. Graficar la secuencia con los máximos y mínimos en un mismo gráfico, indicando con leyendas y etiquetas que representan.

## Ejercicio_3
Se requiere cargar un archivo de audio para extraer información que permitan caracterizar su contenido.
1. Cargar el archivo de audio y leer su metadata.
2. Obtener los valores máximos y mínimos.
3. Obtener el valor promedio de la señal y representarlo mediante una línea horizontal en el gráfico.

## Ejercicio_4
Crear una función para aplicar la convolución entre dos señales de audio (Por ejemplo usando [numpy.convolve](https://numpy.org/doc/1.19/reference/generated/numpy.convolve.html) y [scipy.signal.fftconvolve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html#scipy.signal.fftconvolve)). La función debe ser capaz de elegir un método u otro en función de la cantidad de muestras de cada señal(> 500).

Debe cumplir con: 
* Dos argumentos de entrada como mínimo: audioData_1 (valores de amplitud de la señal 1) y audioData_2 (valores de amplitud de la señal 2).
* Un argumento de salida: audioData_convol (valores de amplitud de la señal resultante de la convolución)
