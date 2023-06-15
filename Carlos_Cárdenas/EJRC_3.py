from carga_archivos import carga_wav
from valor_medio import promedio

def audio(nombre):
    """
   Carga un archivo de audio y calcula su valor máximo, su valor mínimo y su valor promedio.

    Parámetros
    ----------
    nombre : str
        Nombre del archivo de audio.


    Returns
    -------
    valor medio : float.
        Flotante con la información del valor medio.

    """
    # Cargar los archivos de audio
    audios = carga_wav([nombre])
    data_audio1, fs_RI1 = audios.get(nombre)

    # Calcular el valor medio de la señal, elmax y el min
    valor_medio = promedio(data_audio1)
    maximo=max(data_audio1)
    minimo=min(data_audio1)
    
    # Imprimir los valores
    print('El valor máximo de la señal de audio es:', maximo)
    print('El valor mínimo de la señal de audio es:', minimo)
    print('El valor medio de la señal de audio es:', valor_medio)
    return valor_medio
    
    
if __name__ == "__main__":
    from graficar_vm import graficar_vm

    au = audio("sine_sweep.wav")
    graficar_vm(au)
