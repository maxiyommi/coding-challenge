# **Code Review: Coding Challenge - Python**

## Resumen

¡Hola Valentin! Estuve revisando la entrega de tu challenge y quiero compartir con vos algunos comentarios y sugerencias junto a la devolución.

## Objetivos del challenge

### Nota: 6


### Consignas

- [✓] Ejercicio_1
- [✓] Ejercicio_2  
- [X] Ejercicio_3
- [✓] Ejercicio_4  

### Aspectos positivos

- 

### Áreas de mejora

1. **Presentación**: 
 

2. **Resultados**: En el ejercicio 3 llamste a una funcion como promedio y a una varibl tambien como promedio, lo que causaba que se sobreescrbiera la misma y asi crasheaba.


3. **Detalles**: EL principal error fue el uso del if __name__ == "__main__":... y del importe de los .py. La idea era hacer funciones en los .py y correrlas en el main, en tu caso corriste todo el .py lo cual no esta mal. Lo que si es que al poner el condicional del __name__ al comienzo de los scripts no permitia que se corran correctamente desde el main. Es decir, adentro del condicional va solo lo que NO queres que se corra desde el main pero si cuando corres el ejercicio directamente, usualmente siendo pruebas para ir testeando cada ejercicio por separado. Para una explicación mas detallada te dejo un link https://realpython.com/if-name-main-python/ que explica muy bien como ese condicional tan sencillo permite un espacio de trabajo mucho mas ordenado.


### Conclusiones

En general, se notan los conceptos basicos necesarios pero varios detalles mas conceptuales evitaron un funcionamiento esperado del código.

¡Seguí adelante y seguí mejorando tus habilidades!

Si tenés alguna pregunta o necesitás aclaraciones adicionales, no dudes en preguntar.

Saludos,
Gonzalo Rodriguez Jannots.