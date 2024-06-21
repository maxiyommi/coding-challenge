import sympy as sp
from sympy import limit, integrate



def generatePiecewiseFunc():
    """
    Genera una función escalonada a trozos utilizando la biblioteca SymPy.

    Esta función define una función escalonada a trozos utilizando la biblioteca SymPy. La función toma como entrada los símbolos `t` y `T`, que representan la variable independiente y el rango de tiempo, respectivamente.

    **Devuelve:**

    La función escalonada a trozos representada como una expresión simbólica de SymPy.

    **Ejemplo de uso:**

    ```python
    f_a_trozos = generatePiecewiseFunc()
    print(f_a_trozos)
    ```

    **Explicación del código:**

    1. **Importar símbolos:**
        - Se importan los símbolos `t` y `T` de la biblioteca SymPy, representando la variable independiente y el rango de tiempo, respectivamente.

    2. **Definir puntos de quiebre:**
        - Se definen las variables `t1`, `t2` y `t3` que representan los puntos de quiebre de la función escalonada a trozos.

    3. **Definir funciones y sus límites:**
        - Se definen las funciones `f1`, `f2`, `f3` y `f4` utilizando la expresión `sp.Piecewise` de SymPy.
        - Cada función representa un segmento de la función escalonada a trozos en un intervalo específico.
        - Los límites de cada intervalo se definen utilizando expresiones booleanas que comparan `t` con los puntos de quiebre.

    4. **Juntar las funciones:**
        - Se utiliza la función `sp.Piecewise` de SymPy para combinar las funciones `f1`, `f2`, `f3` y `f4` en una única función escalonada a trozos.

    5. **Devolver la función:**
        - Se devuelve la función escalonada a trozos representada como una expresión simbólica de SymPy.
    """
    # Importo el simbolo que será reconocido como variable
    t, T= sp.symbols('t T')

    # Defino los puntos de quiebre de la función
    t1 = 0
    t2 = 1
    t3 = 2

    # Defino las funciones y sus limites
    f1 = (0, t <= t1)
    f2 = (t, (t1<t) & (t<=t2))
    f3 = (2-t, (t2<t) & (t<t3))
    f4 = (0, (t>=t3))

    # Junto todas las funciones con Piecewise
    f_a_trozos = sp.Piecewise(f1,f2,f3,f4)
    return f_a_trozos

def calcEnergiaPotencia(f_a_trozos):
    """
    Calcula y muestra la energía total y la potencia promedio de una función escalonada a trozos representada por `f_a_trozos`.

    **Argumentos:**

    - `f_a_trozos` (SymPy expression): La función escalonada a trozos representada como una expresión simbólica de SymPy.

    **Retorno:**

    No se devuelve ningún valor, pero la función imprime los valores de energía total y potencia promedio en la consola.

    **Ejemplo de uso:**

    ```python
    f_a_trozos = generatePiecewiseFunc()
    calcEnergiaPotencia(f_a_trozos)
    ```

    **Explicación del código:**

    1. **Importar símbolos:**
        - Se importan los símbolos `t` y `T` de la biblioteca SymPy, representando la variable independiente y el rango de tiempo, respectivamente.

    2. **Calcular la energía:**
        - Se utiliza la función `integrate` de SymPy para calcular la integral del valor absoluto al cuadrado de la función `f_a_trozos` en el intervalo de tiempo infinito (-∞, ∞).
        - El resultado de la integral representa la energía total de la señal.
        - Se utiliza el método `evalf()` de SymPy para evaluar la expresión simbólica y obtener un valor numérico aproximado.
        - Se imprime el valor de la energía total en la consola.

    3. **Calcular la potencia:**
        - Se utiliza la función `limit` de SymPy para calcular el límite de la integral del valor absoluto al cuadrado de la función `f_a_trozos` en el intervalo de tiempo infinito (-∞, ∞) cuando `T` tiende a infinito.
        - El resultado del límite representa la potencia promedio de la señal.
        - Se utiliza el método `evalf()` de SymPy para evaluar la expresión simbólica y obtener un valor numérico aproximado.
        - Se imprime el valor de la potencia promedio en la consola.
    """
    t, T= sp.symbols('t T')
    # Calculo la energía 
    energia = integrate(abs(f_a_trozos)**2,(t,-sp.oo, sp.oo))
    # Muestro el valor de energía total
    print(f'Energía Total: {energia.evalf()}')

    # Calculo la potencia
    potencia = limit((1/(2*T)*integrate(abs(f_a_trozos)**2,(t,-sp.oo, sp.oo))),T,sp.oo)
    # Muestro el valor de potencia promedio
    print(f'Potencia Promedio: {potencia.evalf()}')


    
    


