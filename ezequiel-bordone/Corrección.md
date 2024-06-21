# Nota Final: 7 (Siete)

Observación: La idea era desde el main ejecutar las funciones, no solo importarlas para que se ejecuten los .py. Ademas, en el ej2 nunca se llamo a la función por lo que no se corre nunca.

## Ejercicio 1

1. Correcto
2. Correcto
3. Incorrecto: La energía es 0.66 y la potencia 0.

## Ejercicio 2

1. Correcto
2. Correcto
3. Correcto

## Ejercicio 3

1. Incorrecto: Con Metadata se refiere a información que se le puede agregar al wav, como artista, título, genero, bitrate, duración (sin la necesidad de calcularlo) y muchos mas. 
2. Correcto
3. Correcto

## Ejercicio 4

1. Incorrecto: Quedó al reves, si las señales son cortas se usa np.convolve y si son largas ffrconvolve. Ademas se deberían analizar los largos de ambas señales. Tambien, quedó {if len(audio1) < '500':} donde len(audio1) es un int por lo que da error al querer compararlo con '500' que es un str.