<h1 align='center'>
<b>Proyecto MVP de un sistema de recomendación de películas</b>
</h1>

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
- La cantidad de filmaciones, el exito (retorno) y el promedio del retorno de un actor en particular.
- El exito total (retorno) y todas las películas (por cada una la fecha de lanzamiento, el retorno, el costo y la ganancia) de un director en particular.

Por último se va a agregar un nuevo endpoint a la API que es el sistema de recomendación. 

## Requisitos
- Python 3.11 o superior
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

Contiene los archivos de datos utilizados en el proyecto. Adentro hay una carpeta llamada credits y un archivo csv llamado 'movies_dataset.csv'. Dentro de la carpeta credits hay dos archivos parquet. Uno se llama cast.parquet y el otro se llama crew.parquet. 

Originalmente los datos de los dos archivo parquet estaban en un archivo csv llamado credits.csv. Este archivo supera el maximo de 100 Mb que puede tener un archivo para subirse a GitHub. En otra carpeta, distinta del proyecto, cree una notebook, lo converti en un dataframe y luego lo exporte a un archivo parquet llamado credits.parquet. Pero surgio otro problema, aunque menos grave. GitHub recomienda que los archivos no superen los 50 Mb y credits.parquet lo superaba.

Aunque lo puedo subir a GitHub quiero cumplir con el tamaño recomendado de los archivos. El archivo credits.csv tiene tres columnas: cast, crew y id. Lo dividi en dos dataframes. El primero contiene la columna cast y la columna id. El segundo contiene la columna crew y la columna id. Luego exporte ambos dataframe para convertirlos en archivos parquet. Comparten la misma columna id para que no se pierda la relacion entre la columna cast y crew.

El otro archivo csv llamado movies_datasets.csv lo deje como estaba porque no supera los 50 Mb.

- `notebooks/`: 

Contiene los notebooks de jupyter con sus modelos y el analisis.

- `src/`: 

Contiene el código fuente del proyecto, los scripts y los modulos.

- `reports/`: 

Contiene los informes y visualizaciones generados.

- `README.md`: 

Es el archivo donde esta la documentación del proyecto.

## Datos y Fuentes

## Metodología

## Resultados y Conclusiones

## Contribución y Colaboración

## Licencia