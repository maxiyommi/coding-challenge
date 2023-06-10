# 🚀 Coding Challenge - Python 🐍 
¡Bienvenidos al desafío de Python del curso de [Señales y Sistemas de la UNTREF](https://github.com/maxiyommi/signal-systems)! En este desafío, los alumnos tendrán la oportunidad de demostrar sus habilidades en programación utilizando Python. Cada solución deberá ser enviada mediante un Pull Request en este repositorio público a una rama específica.

## Instrucciones 📝
La consigna se encuentra en la carpeta `/consignas` en un archivo .md con nombre de la fecha del corriente año (Ej:`/consignas/junio_2023.md`)
1. Cada alumno deberá hacer un [Fork](fork_doc.md) de este repositorio público.
2. Dentro de su Fork, cada alumno deberá crear una rama con su nombre y apellido en minúsculas separados por guiones medios: <nombre_alumno>-<apellido_alumno>.
    * Por ejemplo: juan-perez
3. Dentro de su rama, cada alumno deberá crear una carpeta con su nombre y apellido en minúsculas separados por guiones bajos.
    * Por ejemplo: juan_perez
4. Dentro de su carpeta personal, los alumnos deben agregar los archivos de su solución (todos los necesarios para reproducir su respuesta).
    * Por ejemplo: ejercicio_1.py
5. Una vez que hayas terminado tu solución, crea un Pull Request para enviarla.

## Estructura del Repositorio 📂
El repositorio tendrá la siguiente estructura:
``` markdown
- master
  - readme.md
- branch <nombre_alumno>-<apellido_alumno>
  - <nombre_alumno>_<apellido_alumno>
    - ejercicio_1.py
- ...
```

## Cómo enviar tu solución mediante un Pull Request  📤
1. Haz un [Fork](fork_doc.md) de este repositorio público.
2. Clona tu Fork en tu máquina local utilizando el comando:
``` bash
git clone <url_del_repositorio>
```
3. Ingresar a la carpeta clonada.
``` bash
cd <nombre_de_carpeta>
```
4. Crea una nueva rama utilizando tu nombre y apellido:
``` bash
git checkout -b <nombre_alumno>-<apellido_alumno>
```
5. Crea una carpeta con tu nombre y apellido en minúsculas separados por guiones bajos.
``` bash
mkdir <nombre_alumno>_<apellido_alumno>
```
6. Agrega tu solución dentro de la carpeta personal que creaste.
    * Asegúrate de utilizar el nombre del ejercicio, por ejemplo: ejercicio_1.py.
7. Haz commit de los cambios y empuja tu rama al repositorio remoto.
``` bash
git add .
git commit -m "Agregando solución de <nombre_alumno>"
git push origin <nombre_alumno>-<apellido_alumno>
```
8. En tu Fork del repositorio, abre un nuevo Pull Request: Ve a la página de tu Fork en GitHub y verás un mensaje resaltado que indica que has hecho recientemente un push a tu rama. Haz clic en el botón "Compare & pull request" que aparece junto al mensaje.
9. Envía el Pull Request: Haz clic en el botón "Create Pull Request" para enviar tu Pull Request al repositorio original.

¡Eso es todo! Has enviado con éxito un Pull Request al repositorio original. Los revisores podrán ver tus cambios, comentar y fusionarlos con el repositorio principal si los consideran apropiados.

Recuerda que durante el proceso de revisión, es posible que te soliciten hacer cambios adicionales. Puedes realizar estos cambios en tu rama local, hacer push nuevamente y los cambios se reflejarán automáticamente en tu Pull Request.

Buena suerte y diviértete resolviendo el desafío de Python. ¡Esperamos ver tus resultados! Si tienes alguna pregunta, no dudes en comunicarte. 🎉👩‍🏫👨‍🏫