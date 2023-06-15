# **Code Review: Coding Challenge - Python**

## Resumen

¡Hola <nombre-alumno>! Estuve revisando la entrega de tu challenge y quiero compartir con vos algunos comentarios y sugerencias junto a la devolución.

## Objetivos del challenge

### Nota: 6


### Consignas

- [✓] Ejercicio_1
- [✓] Ejercicio_2  
- [✓] Ejercicio_3
- [✓] Ejercicio_4  

### Aspectos positivos

- Resultados correctos

### Áreas de mejora

1. **Presentación**: Se debe revisar el uso del if __name__ == "__main__": ..., porque se intenta implementar pero se logra correctamente. https://realpython.com/if-name-main-python/ ahi poder revisarlo mejor y ver para que sirve. Por otro lado los docstrings se utilizan para cada funcion, es decir def funcion(), no para cada .py. 


2. **Resultados**: "num_muestras or num_muestras_1 > 500:" Esta linea no hace lo que se espera a simple vista, en realidad esta haciendo una operación binaria entre (num_muestras or num_muestras_1) y despues comparando eso con 500. la forma correcta es hacer 2 condicionales (num_muestras > 500) (num_muestras_1 > 500) y despues la funcion "or" entre esas 2. 
 

3. **Detalles**: La imposibildiad de usar github, como ya se habló, es una herramienta dificil al principio pero vital a la hora de trabajar de a grupo.


### Conclusiones

En general, Se llego a los resultados pero con varias dificultades del orden conceptual de detalles mas que de código. Igualmente, esos "detalles" son imprecindibles a la hora de trabajar en un proyecto mas complejo y de a grupo, por lo que se deberían revisar en profundidad.

¡Seguí adelante y seguí mejorando tus habilidades!

Si tenés alguna pregunta o necesitás aclaraciones adicionales, no dudes en preguntar.

Saludos,
Gonzalo Rodriguez Jannots.