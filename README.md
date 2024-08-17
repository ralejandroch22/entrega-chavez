# Entrega-Chavez

## Video Demostrativo:


Instalacion:

1. En la consola de VS code, ubicarse en la carpeta PDStock con el comando: **cd PDStock**
2. Luego especificar la version de python version 3.9.13, ejecutar: **pipenv --python 3.9.13**
3. Luego crear un entorno virtual: **pipenv shell**
4. Instalar el archivo de requirements.txt: **pipenv install -r requirements.txt**
5. Ejecutar el servidor: **python manage.py runserver**

## Sobre el proyecto:

Quise basarme en el sistema de stock de la empresa en donde trabajo como programador.

Primero el usuario debera estar logueado ingresando en Cuenta/Log in o Crear cuenta.

Como usuario podra ver el stock cargado en la empresa desde la seccion Items/Todos o podra buscar el articulo que necesite

Desde el boton Ver, podra ver mas detalles como el precio o marca.

Como usuario podra editar su perfil para agregar su nombre, apellido, mail y cargar su avatar. El sistema le precarga un avatar con sus iniciales si decide no cargar una imagen. Tambien puede cambiar su contraseña desde la misma seccion de editar el perfil.

El usuario administrador puede hacer todas estas funciones, pero adicionalmente puede cargar items al stock, editar cualquier item cargado o borrarlo.
