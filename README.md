<h1 align='center'>
<b>Proyecto MVP de un sistema de recomendación de películas</b>
</h1>

## Datos del proyecto:

Autor: Francisco Hugo Lezik

Academia: Henry

Curso: Data Science Part Time

Cohorte: 11

Correo: franciscohugolezik@gmail.com

URL de linkedin: https://www.linkedin.com/in/francisco-hugo-lezik-7b4256220/

Página web: https://proyecto-peliculas-wnuw.onrender.com/docs

## Tabla de contenido

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Estructura](#estructura)
5. [Ejecución](#ejecución)
6. [Datos y Fuentes](#datos-y-fuentes)

## Introducción

El objetivo de este proyecto de MVP (Minimum Viable Product) es crear una aplicacion web o API, en Render, de un sistema de recomendación de películas. El objetivo es acceder a los datos guardados en los datasets a traves de seis endpoints.

Los endpoints son:

- La cantidad de filmaciones por mes.

- La cantidad de filmaciones por día.

- El estreno y el score de una película en particular.

- El año, la cantidad de votos y el promedio de los votos de una película en particular.

- La cantidad de peliculas, el exito o retorno (suma del retorno de todas las peliculas) y el promedio del retorno de todas las peliculas de un actor en particular. (1)

- El exito total (retorno) y todas las películas (por cada una: la fecha de lanzamiento, el retorno, el presupuesto y los ingresos) de un director en particular. (2)


(1) Durante el proceso de la elaboracion de este endpoint se descubrio que faltaban datos del retorno de varias peliculas por lo que se opto por incluir la cantidad total de peliculas y la cantidad de las peliculas que poseen datos sobre el retorno. Se uso el retorno de las peliculas que lo tenian. Por ejemplo:

Si el actor participo de 10 peliculas y 5 de ellas tienen el dato del retorno, entonces, se usaran los datos del retorno de estas últimas 5.

(2) El problema del anterior endpoint afecta tambien a este endpoint. Por lo tanto se decidio usar la solucion dada en el punto anterior (2).

#

## Requisitos

Python 3.11.9
Las librerías necesarias estan en venv_requirements.txt.

#

## Instalación

1. Clonar el repositorio: 
    `git clone https://github.com/FranciscoHugoLezik/Proyecto_Peliculas/tree/branch_1` 

2. Crear un entorno virtuak: `python -m venv venv`

3. Activar el entorno virtual:
    - Windows: `venv\Scripts\activate` (Si se usa Git bash es: `source venv/Scripts/activate`)

    - macOS/Linux: `source venv/bin/activate`

4. Instalar las dependencias: `pip install -r venv_requirements.txt`

La libreria requirements.txt es para Render.

#

## Estructura

- `data/`: 

En la carpeta data/ se guardan los datasets procesados por ETL. A continuacion se lista el contenido:

cast.parquet

crew.parquet

movies_ETL.parquet

#

- `notebooks/`: 

Contiene el EDA y los ETL de los archivos en crudo. Los archivos en crudo son extraidos de un repositorio en GitHub llamado Movies_data. Los archivos producidos por los ETL son alojados en las carpeta data. Cada ETL guarda el archivo en una ubicacion ya establecida. 

El link del repositorio Movies_data es:

https://github.com/FranciscoHugoLezik/Movies_data.git

Contiene cuatro notebooks:

- EDA.ipynb

- ETL_cast_id.ipynb

- ETL_crew_id.ipynb

- ETL_movies.ipynb

#

- `src/`: 

Contiene el código fuente del proyecto. Dentro se encuentran dos carpetas y un archivo main.py que contiene la api:

* Carpeta __modules__ : contiene los modulos. Hay tres carpetas.

    * Carpeta __credits__: contiene dos carpetas.

        * Carpeta __functions__: contiene dos modulos: get_actor y get_director. Cada una tiene una funcion principal. Son importados por los endpoints get_actor y get_director, respectivamente.

        * Carpeta __helpers__: contiene tres modulos auxiliares: filtrar_con_retorno, get_creditos y procesar_peliculas. Cada una tiene una funcion auxiliar. Son importados por los modulos de la carpeta functions.

    * Carpeta __movies__: contiene dos carpetas.

        * Carpeta __functions__: contiene cuatro modulos: cantidad_filmaciones_dia, cantidad_filmaciones_mes, score_titulo y votos_titulo. Cada una tiene una funcion principal. Son importados por los endpoints cantidad_filmaciones_dia, cantidad_filmaciones_mes, score_titulo y votos_titulo, respectivamente.

        * Carpeta __helpers__: contiene cinco modulos auxiliares: get_dia_en_ingles, get_dias, get_filmacion, get_meses y get_numero_del_mes. Cada una tiene una funcion auxiliar. Son importados por los modulos de la carpeta functions.

    * Carpeta __others__: ccntiene otros dos modulos auxiliares: constants y import_file. Una tiene constantes y la otra una funcion de importacion de datasets. Son importados por varios modulos.

* Carpeta __scripts__ : contiene los scripts. Hay dos carpetas y un script. Este script suelto contiene los datos del autor de la página web.

    * Carpeta __credits__: contiene dos scripts: get_actor y get_director. Son routers y son importados por la api del archivo main.py.

    * Carpeta __movies__: contiene cuatro scripts: cantidad_filmaciones_dia, cantidad_filmaciones_mes, score_titulo y votos_titulo. Son routers y son importados por la api del archvo main.py.

main.py : Contiene la API.

#

- `tests/`: contiene dos archivos py que testean las funciones auxiliares: credits_helpers y movies_helpers.

#

- `.gitignore`:

Es el archivo que permite que git no haga un commit de los archivos o carpetas. Esto se logra escribiendo la ubicacion del archivo o de la carpeta. Se comienza a partir de la raíz de la carpeta del proyecto. Por ejemplo: Para que git no haga un commit del entorno virtual se escribe en el archivo .gitignore la ubicacion /venv ya que esta carpeta esta en la raiz de la carpeta del proyecto. 

#

- `README.md`: 

Es el archivo donde esta la documentación del proyecto.

#

- `venv_requirements.txt`: 

Es el archivo que contiene las librerias que use en mi entorno virtual. Decidi tener este archivo separado porque Render me daba muchos problemas con las versiones de las librerias.

#

- `requirements.txt`:

Es el archivo que contiene las librerías que le indican a Render que versiones usar. Ya esta probada. No deberia dar error.

#

## Ejecución

En la carpeta notebooks se encuentran los ETL. Se los puede ejecutar para producir los archivos requeridos que se guardan en la carpeta data/. Es opcional porque ya estan ejecutadas. 

#

## Datos y Fuentes

En un principio los archivos en crudo iban a estar en la carpeta data/.

Como el proyecto se carga en Render y se usa la version gratuita, que tiene un RAM de 512 Mb, se tuvo que poner los archivos en crudo en otro repositorio, de github, llamado Movies_data. Los archivos ETL descargan los archivos de ese repositorio. En el readme de ese repositorio explico el proceso que se tuvo que hacer para poder exportalos a GitHub.

El GitHub del repositorio de los archivos en crudo es:

https://github.com/FranciscoHugoLezik/Movies_data.git

Datasets en crudo:

__cast.parquet__ : originalmente dentro de credits.csv. Contiene los datos anidados de cada uno de los actores de cada pelicula.

__crew.parquet__ : originalmente dentro de credits.csv. Contiene los datos anidados de cada uno de los miembros del equipo de produccion de cada pelicula.

__movies_dataset.parquet__ : originalmente era un archivo csv. Contiene los datos de cada pelicula.

El proceso de ETL produjo 3 datasets almacenados como archivos parquet. Estan guardados en la carpeta data/:

__cast.parquet__ : contiene los datos de los actores de forma individual. Se pueden repetir por el id de la pelicula si participaron en mas de una pelicula.

__crew.parquet__ : contiene los datos de los miembros del elenco de forma individual. Se pueden repetir por el id de la pelicula si participaron en mas de una pelicula.

__movies.parquet__ : contiene los datos de cada pelicula sin las columnas de datos anidados.