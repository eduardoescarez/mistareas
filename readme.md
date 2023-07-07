# Mis tareas

## Introducción

Mis Tareas es una aplicación web para la gestión de tareas pendientes, desarrollado en el lenguaje de programación Python con el framework Django. Utiliza como gestor de base de datos PostgreSQL.

## Estructura de directorios

La estructura de directorios es la siguiente

- mainsite : Contiene los archivos de la pagina principal, estilos, archivos estáticos.
- mistareas : Contiene la aplicación web Mis Tareas
- sitioweb : Contiene las configuraciones base del proyecto de Django


## Instalación

1.  Para instalar el sistema primero cree un entorno virtual mediante el comando

        python -m venv .venv

2.  Después, active el entorno virtual

        .venv\scripts\activate

3.  Clone el proyecto usando el archivo ZIP desde Github Y descomprima el archivo **en el mismo directorio** donde se encuentra el directorio .venv. También puede clonar el proyecto usando git, con las indicaciones señaladas anteriormente.

4.  y utilice el siguiente comando para instalar los requisitos de sistema:

        (.venv) píp install -r requeriments.txt

5.  Cree un archivo .env en el directorio raíz del sistema y proporcione los datos para acceder a una base de datos de PostgreSQL:

        SECRET_KEY= 'Secret_key'     # secret_key de Django
        DB_ENGINE= 'django.db.backends.postgresql_psycopg2'
        DB_DATABASE= 'database'      # Nombre de la base de datos
        DB_USER= 'user'              # Usuario de la base de datos
        DB_PASSWORD= 'password'      # Contraseña del usuario 
        DB_HOST= 'host'              # Dirección del servidor PostgreSQL 
        DB_PORT= '5432'              # Puerto del servidor PostgreSQL, habitualmente 5432

6.  Finalmente para ejecutar el proyecto utilice el comando
        (.venv) python manage.py runserver

## Estructura de directorios principales

Los directorios principales de Django son:

- website: Contiene las configuraciones principales, rutas, vistas
- mainsite: Contiene las paginas públicas del sitio web y sus archivos estáticos y plantillas
- telovendo: Contiene la aplicación interna para usuarios, modelos y relacionados

También existe una carpeta adicional **docs** que contiene otros archivos de documentación de la aplicación.

## Usuarios

Los usuarios disponibles en esta aplicación son:

    Superadministrador

    username   : admin
    contraseña : hola.123
    email      : admin@mistareas.cl

    Usuario
    
    username   : mmacjob
    contraseña : CARONTE23
    email      : mcornejo@migato.cl

    Usuario
    
    username   : isantamaria
    contraseña : CARONTE23

    Usuario
    
    username   : mmoragues
    contraseña : CARONTE23
    