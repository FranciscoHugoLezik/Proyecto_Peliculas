<h1 align='center'>
<b>Proyecto MVP de un sistema de recomendación de películas</b>
</h1>

## Autor: Francisco Hugo Lezik

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

## Instalación
1. Clonar el repositorio: 
    `git clone https://github.com/FranciscoHugoLezik/Proyecto_Peliculas.git` 

2. Crear un entorno virtuak: `python -m venv venv`

3. Activar el entorno virtual:
    - Windows: `venv\Scripts\activate` (Si se usa Git bash es: `source venv/Scripts/activate`)

    - macOS/Linux: `source venv/bin/activate`

4. Instalar las dependencias: `pip install -r requirements.txt`

## Estructura

- `data/`: 

En un principio los archivos en crudo también iban a estar en esta carpeta. El proyecto se carga en Render. Uso la version gratuita que tiene un RAM de 512 Mb. Por este motivo los tuve que poner en otro repositorio de github llamado Movies_data. Los archivos ETL descargan los archivos de ese repositorio. En el readme de ese repositorio explico el proceso que tuve que hacer para poder exportalos a GitHub.

El GitHub del repositorio de los archivos en crudo es:

https://github.com/FranciscoHugoLezik/Movies_data.git

En esta carpeta se guardan los archivos que son el resultado del proceso ETL de los archivos en crudo. Dentro de esta carpeta se encuentran dos subcarpetas: 

    - credits
    - movies_dataset

Carpeta credits: Contiene dos archivos que estaban anidados en el archivo en crudo original llamado credits.parquet.

Estos archivos son los siguientes:

    - cast_ETL.parquet
    - crew_ETL.parquet

Descripcion de cada una:

    - cast_ETL.parquet

        Este archivo contiene los datos de los actores que participaron en cada pelicula. Dentro de este archivo se encuentran las siguientes columnas:

            - cast_id
            - character
            - credit_id
            - gender
            - id
            - name
            - order
            - profile_path
            - movie_id

        Todas estas columnas tienen valores de tipo object (pandas llama object al tipo str).

    - crew_ETL.parquet

        Este archivo contiene los datos de los miembros del equipo de produccion de cada pelicula. Dentro de este archivo se encuentran las siguientes columnas:

            - credit_id
            - department
            - gender
            - id
            - job
            - name
            - profile_path
            - movie_id

        Todas estas columnas tienen valores de tipo object (pandas llama object al tipo str).

Carpeta movies_dataset: Contiene una carpeta y un archivo. Originalmente los datos de estos archivos se encontraban en el archivo original en crudo llamado movies_dataset.parquet.

La carpeta y el archivo son:

    - Carpeta extracted_tables
    - movies_ETL.parquet:

Descripción de cada una:

    - Carpeta extracted_tables: Contiene cinco archivos. Los datos de estos archivos estaban anidados. Fueron extraidos para poder acceder a estos datos de forma rapida y sin complicaciones.

    Los archivos son:

        - belongs_to_collection_ETL.parquet : Contiene los datos de cada franquicia.
        
        Sus columnas son:

            - id
            - name
            - backdrop_path
            - movie_id

            Todas de tipos object(str).

        - genres_ETL.parquet : Contiene los datos de cada genero.

        Sus columnas son:

            - id
            - name
            - movie_id

            Todas son de tipo object(str).

        - production_companies_ETL.parquet : Contiene los datos de cada compañia.

        Sus columnas son:

            - name
            - id
            - movie_id

            Todas son de tipo object(str).

        - production_countries_ETL.parquet : Contiene los datos de cada pais.

        Sus columnas son:

            - iso_3166_1
            - name
            - movie_id

            Todas son de tipo object(str).

        - spoken_language_ETL.parquet : Contiene los datos de cada idioma.

        Sus columnas son:

            - iso_639_1
            - name
            - movie_id

            Todas son de tipo object(str).

    - movies_ETL.parquet: Este archivo contiene los datos de cada pelicula sin los datos anidados.
    Dentro de este archivo se encuentran las siguientes columnas:

        - budget: tipo int64.
        - id: tipo object.
        - original_language: tipo object.
        - overview: tipo object.
        - popularity: tipo float64.
        - release_date: tipo datetime64[ns].
        - revenue:    tipo int64.
        - runtime: tipo float64.
        - status: tipo object.
        - tagline: tipo object.
        - title: tipo object.
        - vote_average: tipo float64.
        - vote_count: tipo int32.
        - release_year: tipo int32.
        - return: tipo float64.


- `notebooks/`: 

Contiene los notebooks de jupyter con sus modelos y el ETL.



- `reports/`: 

Contiene los informes y visualizaciones generados.

- `src/`: 

Contiene el código fuente del proyecto, los scripts y los modulos.

- `.gitignore`:

Es el archivo que permite que git no haga un commit de los archivos o carpetas. Esto se logra escribiendo la ubicacion del archivo o de la carpeta. Se comienza a partir de la raíz de la carpeta del proyecto. Por ejemplo: Para que git no haga un commit del entorno virtual se escribe en el archivo .gitignore la ubicacion /venv ya que esta carpeta esta en la raiz de la carpeta del proyecto. 

- `README.md`: 

Es el archivo donde esta la documentación del proyecto.

- `requirements.txt`:

Es el archivo que contiene las librerías que deben estar instaladas en el entorno virtual.

## Ejecución



## Datos y Fuentes

## Metodología

## Resultados y Conclusiones

## Contribución y Colaboración

## Licencia