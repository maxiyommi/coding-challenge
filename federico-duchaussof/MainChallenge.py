import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.io import wavfile
from Ejercicio_1_challenge import f_cuadrado, calcular_potencia_infinito, f
from Ejercicio_2_challenge import secuencia_aleatoria, maximo_y_minimo
from Ejercicio_3_challenge import metadata, calcular_promedio
from Ejercicio_4_challenge import convolucion_audio, plot_convolucion_audio

def main(x, num_elementos, min_valor, max_valor, seed=None, secuencia=None, ruta=None, y=None, audioFile_1=None, audioFile_2=None):
    """
    Función principal que integra las funcionalidades de los cuatro ejercicios.

    Parámetros:
        x (float): Valor de entrada para la función f(x).
        num_elementos (int): Número de elementos para la secuencia aleatoria.
        min_valor (float): Valor mínimo para la secuencia aleatoria.
        max_valor (float): Valor máximo para la secuencia aleatoria.
        seed (int or None): Semilla para la generación de números aleatorios (opcional).
        secuencia (numpy.ndarray): Secuencia aleatoria pregenerada (opcional).
        ruta (str): Ruta al archivo de audio WAV (opcional).
        y (numpy.ndarray): Señal de audio precargada (opcional).
        audioFile_1 (str): Ruta al primer archivo de audio WAV para la convolución.
        audioFile_2 (str): Ruta al segundo archivo de audio WAV para la convolución.

    Nota: Los parámetros opcionales permiten utilizar valores predefinidos o precargados para cada ejercicio.
    """

    # Ejercicio 1: Análisis de la función f(x)
    Energia, error = integrate.quad(f_cuadrado, 0, 2)
    print(f"La energía total es: {Energia}")

    potencia = calcular_potencia_infinito(f)
    print(f"La potencia de la función f(x) es: {potencia}")

    # Ejercicio 2: Análisis de una secuencia aleatoria
    if secuencia is None:
        secuencia = secuencia_aleatoria(num_elementos, min_valor, max_valor, seed=seed)

    maximo, minimo = maximo_y_minimo(secuencia)

    plt.figure(figsize=(10, 6))
    plt.plot(secuencia, label='Secuencia aleatoria')
    plt.scatter(maximo, secuencia[maximo], label=f'maximo ({secuencia[maximo]:.2f})')
    plt.scatter(minimo, secuencia[minimo], label=f'minimo ({secuencia[minimo]:.2f})')
    plt.title('Secuencia Aleatoria')
    plt.xlabel('Indice')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()

    # Ejercicio 3: Análisis de una señal de audio
    if ruta is not None:
        sr, y = wavfile.read(ruta)
        duracion, valor_max, valor_min = metadata(ruta)
        valor_promedio = calcular_promedio(y)

        tiempo = np.arange(len(y)) / float(sr)
        plt.figure(figsize=(12, 6))
        plt.plot(tiempo, y, label='Señal de audio')
        plt.axhline(valor_promedio, color='g', label='Valor promedio')
        plt.title('Señal de audio y valor promedio')
        plt.xlabel('Tiempo (segundos)')
        plt.ylabel('Amplitud')
        plt.legend()
        plt.show()

        print(f'Valor promedio: {valor_promedio:.2f}')
        print(f'Valor máximo: {valor_max:.2f}')
        print(f'Valor mínimo: {valor_min:.2f}')
        print(f'Duración del audio: {duracion:.2f} segundos')

    # Ejercicio 4: Convolución de señales de audio
    if audioFile_1 is not None and audioFile_2 is not None:
        audioData_1, tiempo1, audioData_2, tiempo2, audioData_convol, tiempo_conv = convolucion_audio(audioFile_1, audioFile_2)
        
        # Graficar la convolución
        plot_convolucion_audio(audioData_1, tiempo1, audioData_2, tiempo2, audioData_convol, tiempo_conv)

if __name__ == "__MainChallenge__":
    x = 0.5
    num_elementos = 30
    min_valor = 0
    max_valor = 10
    seed = None
    secuencia = None
    y = None
    ruta = 'RuidoRosa.wav'  # Ruta al archivo WAV
    audioFile_1 = 'Sine_Sweep.wav'  # Ruta al primer archivo de audio WAV
    audioFile_2 = 'Filtro_Inverso.wav'  # Ruta al segundo archivo de audio WAV

    main(x, num_elementos, min_valor, max_valor, seed, secuencia, ruta, y, audioFile_1, audioFile_2)