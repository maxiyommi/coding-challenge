# **Code Review: Coding Challenge - Python**

## Resumen

¡Hola Agustin! Estuve revisando la entrega de tu challenge y quiero compartir con vos algunos comentarios y sugerencias junto a la devolución.

## Objetivos del challenge

### Nota: 7 (provisoria)


### Consignas

- [✓] Ejercicio_1
- [✓] Ejercicio_2  
- [✓] Ejercicio_3
- [✗] Ejercicio_4

### Aspectos positivos

- Resultados esperados.
- Rápida resolución y entrega por Git.

### Áreas de mejora

1. **Presentación**: Las funciones no tienen su correspo ndiente docstring. El código funciona en su mayor parte pero una mayor prolijidad no estaría de sobra.
 

2. **Resultados**:

- Ejercicio 1: En el main quedo "display(Function)" siendo display una funcion que no estaba importada por lo que no corria main.py. Al cambiarlo por print() se pudo observar.
- Ejercicio 2: Se printean 2 "9" debido a que quedaron los print dentro de la funcion, generando que se printeen al llamar la función. Deberían salir con un return y ser printeados dentro del "if __name__ ...".
- Ejercicio 4: Hay un error en el condicional ya que "if len(audioData_1) & len(audioData_2) >= 500:" no significa lo que se cree, sino que al hacer "int & int" se esta pasando a binario esos numeros y a cada bit se le está haciendo un "and" entre ambos bits, para luego pasar eso a un valor decimal nuevamente y recipen ahi compararlo con el 500. Esto se puede comprobar al hacer "6 & 0 < 4" y ver que devuelve un True. La forma correcta es hacer 2 condicionales como "if len(audioData_1) >=500 and len(audioData_2) >= 500:". Por otro lado, estaría bueno ver el resultado de la convolución de forma gráfica con señales que se sepa su resultado para observar el correcto funcionamiento.


3. **Detalles**: -


### Conclusiones

En general, se nota una noción de como obtener resultados pero a su vez una falta de prolijidad y correcta documentación, lo que lleva a errores torpes como el printeo de esos "9", por ejemplo. Mas alla de estos erroes se logró alcanzar y analizar los resultados pedidos. 

¡Seguí adelante y seguí mejorando tus habilidades!

Si tenés alguna pregunta o necesitás aclaraciones adicionales, no dudes en preguntar.

Saludos,
Gonzalo Rodriguez Jannots