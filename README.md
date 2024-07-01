Autos DEL MAR Ev3
Este proyecto es una evaluación educativa con código disponible para uso educativo.

Requisitos previos
Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas:

1.Entorno Virtual

Si no tienes creado tu entorno virtual, puedes hacerlo usando el siguiente comando en tu terminal:


py -m venv myvenv

Esto creará un entorno virtual llamado myvenv.


2.Archivo requirements.txt

Crea un archivo requirements.txt y agrega las siguientes dependencias:

Django==4.1.2

django-crispy-forms==1.12.0

Instalación de Dependencias

Ejecuta el siguiente comando para instalar las dependencias listadas en requirements.txt:

pip install -r requirements.txt

3.Instalación adicional

Instala las siguientes bibliotecas adicionales necesarias para el proyecto:

pip install pillow
pip install crispy-bootstrap4



4.Levantar el Proyecto
Para ejecutar el proyecto, sigue estos pasos:

Ejecutar el Servidor

Desde la carpeta del proyecto (ProyectoWeb-Autosdelmar), inicia el servidor de desarrollo con:

python manage.py runserver

Esto iniciará el servidor en http://127.0.0.1:8000/.

5.Acceso al Área de Administrador
Para acceder al área de administrador del proyecto, visita la siguiente dirección en tu navegador:

http://127.0.0.1:8000/admin

Utiliza las siguientes credenciales:

Usuario: AdministradorMar
Contraseña: admin123


Este README proporciona los pasos necesarios para configurar y ejecutar el proyecto "Autos DEL MAR Ev3" en tu entorno local. Asegúrate de seguir estos pasos para comenzar a explorar y desarrollar sobre la aplicación.







