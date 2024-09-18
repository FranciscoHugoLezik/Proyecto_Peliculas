<h1 align='center'>
<b>Proyecto MVP de un sistema de recomendación de películas</b>
</h1>

## Autor:

Este proyecto es de autoría de Francisco Hugo Lezik.

Mi correo es: franciscohugolezik@gmail.com

El URL de mi linkedin es: https://www.linkedin.com/in/francisco-hugo-lezik-7b4256220/

## Tabla de contenido

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Estructura](#estructura)
5. [Ejecución](#ejecución)
6. [Datos y Fuentes](#datos-y-fuentes)
7. [Metodología](#metodología)
8. [Resultados y Conclusiones](#resultados-y-conclusiones)
9. [Contribución y Colaboración](#contribución-y-colaboración)
10. [Licencia](#licencia)

## Introducción

El objetivo de este proyecto de MVP (Minimum Viable Product) es crear un sistema de recomendación de películas. El objetivo es que este sistema recomiende películas similares a una película en particular vista por cada usuario particular. La cantidad de películas a recomendar son cinco. Estas películas deben ser similares en puntuación a la película usada para recomendar. Se mostraran sus títulos ordenadas de mayor puntaje a menor puntaje.

En primer lugar se crea una API con endpoints que satisfagan las siguientes necesidades de los usuarios:

- La cantidad de filmaciones por mes.

- La cantidad de filmaciones por día.

- El estreno y el score de una película en particular.

- El año, la cantidad de votos y el promedio de los votos de una película en particular.

- La cantidad de peliculas, el exito o retorno (suma del retorno de todas las peliculas) y el promedio del retorno de todas las peliculas de un actor en particular. (1)

- El exito total (retorno) y todas las películas (por cada una: la fecha de lanzamiento, el retorno, el presupuesto y los ingresos) de un director en particular. (2)


(1) Durante el proceso de la elaboracion de este endpoint se descubrio que faltaban datos del retorno de varias peliculas por lo que se opto por incluir la cantidad total de peliculas y la cantidad de las peliculas que poseen datos sobre el retorno. Se uso el retorno de las peliculas que lo tenian. Por ejemplo:

Si el actor participo de 10 peliculas y 5 de ellas tienen el dato del retorno, entonces, se usaran los datos del retorno de estas últimas 5.

(2) El problema del anterior endpoint afecta tambien a este endpoint. Por lo tanto se decidio usar la solucion dada en el punto anterior (2).

Por último se va a agregar un nuevo endpoint a la API que es el sistema de recomendación. 

## Requisitos

- Python 3.8.10 o superior
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

#

## Instalación

1. Clonar el repositorio: 
    `git clone https://github.com/FranciscoHugoLezik/Proyecto_Peliculas.git` 

2. Crear un entorno virtuak: `python -m venv venv`

3. Activar el entorno virtual:
    - Windows: `venv\Scripts\activate` (Si se usa Git bash es: `source venv/Scripts/activate`)

    - macOS/Linux: `source venv/bin/activate`

4. Instalar las dependencias: `pip install -r requirements.txt`

#

## Estructura

- `data/`: 

En la carpeta data/ se guardan los archivos que son el resultado del proceso ETL de los archivos en crudo. A continuacion se lista el contenido:

Carpeta __credits/__

- cast_ETL.parquet

- crew_ETL.parquet

Carpeta __movies_dataset/__

- belongs_to_collection_ETL.parquet

- genres_ETL.parquet

- movies_ETL.parquet

- production_companies_ETL.parquet

- production_countries_ETL.parquet

- spoken_language_ETL.parquet

#

- `notebooks/`: 

Contiene los archivos jupyter para el ETL de los archivos en crudo. Los archivos en crudo son extraidos de un repositorio en GitHub llamado Movies_data. Los archivos producidos por los ETL son alojados en las carpeta data. Cada ETL guarda el archivo en una ubicacion ya establecida. 

El link del repositorio Movies_data es:

https://github.com/FranciscoHugoLezik/Movies_data.git

Las carpetas que contiene son las siguientes:

Carpeta __ETL_credits/__ : Contiene el ETL de los archivos en crudo llamados cast_id.parquet y crew_id.parquet. Originalmente estaban en un archivo en crudo llamado credits.csv pero fueron separados y convertidos a parquet para poder guardarlos en github.

Se hicieron dos ETL:

- ETL_cast_id.ipynb

- ETL_crew_id.ipynb

Carpeta __ETL_movies_dataset/__ : Contiene el ETL del archivo en crudo llamado movies_dataset.parquet.

Se hicieron seis ETL:

- ETL_belongs_to_collection.ipynb

- ETL_genres.ipynb

- ETL_movies.ipynb

- ETL_production_companies.ipynb

- ETL_production_countries.ipynb

- ETL_spoken_languages.ipynb

#

- `reports/`: 

Contiene los informes y visualizaciones generados.

#

- `src/`: 

Contiene el código fuente del proyecto. Dentro se encuentran dos carpetas y un archivo main.py:

Carpeta __pycache__ : contiene archivos con el bytecode compilado de los módulos Python. Es generado automaticamente.

Carpeta __Scrips__ : contiene otra pycache y un archivo script. El script es el siguiente:

query_movies.py : Contiene las funciones que hacen el procesamiento requerido por los endpoints alojados en el main.py.

main.py : Contiene la API y los endpoints. Estos endpoints llaman a las funciones alojadas en el script query_movies.py para hacer el procesamiento.

#

- `.gitignore`:

Es el archivo que permite que git no haga un commit de los archivos o carpetas. Esto se logra escribiendo la ubicacion del archivo o de la carpeta. Se comienza a partir de la raíz de la carpeta del proyecto. Por ejemplo: Para que git no haga un commit del entorno virtual se escribe en el archivo .gitignore la ubicacion /venv ya que esta carpeta esta en la raiz de la carpeta del proyecto. 

#

- `README.md`: 

Es el archivo donde esta la documentación del proyecto.

#

- `requirements.txt`:

Es el archivo que contiene las librerías que deben estar instaladas en el entorno virtual.

#

## Ejecución

En la carpeta notebooks se encuentran los ETL. Se los puede ejecutar para producir los archivos requeridos que se guardan en la carpeta data/. Es opcional porque ya estan ejecutadas. 

#

## Datos y Fuentes

En un principio los archivos en crudo iban a estar en la carpeta data/.

El proyecto se carga en Render. Se usa la version gratuita que tiene un RAM de 512 Mb. Por este motivo se tuvo que poner en otro repositorio de github llamado Movies_data. Los archivos ETL descargan los archivos de ese repositorio. En el readme de ese repositorio explico el proceso que se tuvo que hacer para poder exportalos a GitHub.

El GitHub del repositorio de los archivos en crudo es:

https://github.com/FranciscoHugoLezik/Movies_data.git

Datasets en crudo:

__cast_id.parquet__ : originalmente dentro de credits.csv. Contiene los datos anidados de cada uno de los actores de cada pelicula.

__crew_id.parquet__ : originalmente dentro de credits.csv. Contiene los datos anidados de cada uno de los miembros del equipo de produccion de cada pelicula.

__movies_dataset.parquet__ : originalmente era un archivo csv. Contiene los datos de cada pelicula.

El proceso de ETL produjo 8 datasets almacenados como archivos parquet. Estan guardados en la carpeta data/:

__cast_ETL.parquet__ : contiene los datos de los actores de forma individual. Se pueden repetir por el id de la pelicula si participaron en mas de una pelicula.

__crew_ETL.parquet__ : contiene los datos de los miembros del equipo de produccion de forma individual. Se pueden repetir por el id de la pelicula si participaron en mas de una pelicula.

__movies_ETL.parquet__ : contiene los datos de cada pelicula sin las columnas de datos anidados.

__belongs_to_collection_ETL.parquet__ : era una columna en el dataset movies_dataset. Contiene los datos de cada franquicia. Se puede repetir por el id de las peliculas si la franquicia tiene mas de una pelicula.

__genres_ETL.parquet__ : era una columna en el dataset movies_dataset. Contiene los datos de cada tipo de genero. Se puede repetir por el id de las peliculas porque un genero tiene muchas peliculas.

__production_companies_ETL.parquet__ : era una columna en el dataset movies_dataset. Contiene los datos de cada compañia cinematografica. Se puede repetir por el id de las peliculas porque una compañia cinematografica tiene muchas peliculas.

__production_countries_ETL.parquet__ : era una columna en el dataset movies_dataset. Contiene los datos de cada pais en donde se produjo la pelicula. Se puede repetir por el id de las peliculas porque un país tiene muchas peliculas.

__spoken_language_ETL.parquet__ : era una columna en el dataset movies_dataset. Contiene los datos de cada idioma hablado en cada pelicula. Se puede repetir por el id de las peliculas porque un país tiene muchas peliculas.

#

## Metodología



## Resultados y Conclusiones

## Licencia