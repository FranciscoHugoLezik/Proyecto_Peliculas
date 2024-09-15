import pandas as pd
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(base_dir, 'data', 'movies_dataset', 'movies_ETL.parquet')

movies_df = pd.read_parquet(file_path, engine='fastparquet')


def cantidad_filmaciones_mes(mes):
    months = {
        'enero': '1', 
        'febrero': '2', 
        'marzo': '3', 
        'abril': '4', 
        'mayo': '5', 
        'junio': '6', 
        'julio': '7', 
        'agosto': '8', 
        'septiembre': '9', 
        'octubre': '10', 
        'noviembre': '11', 
        'diciembre': '12'
    }
    mes_num = int(months.get(mes))
    meses_series = movies_df['release_date'].dt.month
    meses_list = meses_series.tolist()
    cantidad = meses_list.count(mes_num)
    return (cantidad)


def cantidad_filmaciones_dia(dia):
    dias = {
        'lunes': 'Monday', 
        'martes': 'Tuesday', 
        'miercoles': 'Wednesday', 
        'jueves': 'Thursday', 
        'viernes': 'Friday', 
        'sabado': 'Saturday', 
        'domingo': 'Sunday'
    }
    day = dias.get(dia)
    date = pd.DataFrame(movies_df['release_date'])
    date['nombre_de_dia'] = (date['release_date'].dt.strftime('%A'))
    nombre_de_dia_list = date['nombre_de_dia'].tolist()
    cantidad = nombre_de_dia_list.count(day)
    return (cantidad)


def score_titulo(titulo_de_la_filmación):
    title_year_popularity_df = pd.DataFrame(movies_df[['title','release_year','popularity']])
    title_year_popularity_df.set_index('title', inplace=True)
    year_popularity_series = title_year_popularity_df.loc[titulo_de_la_filmación]
    año = year_popularity_series['release_year']
    año = int(año)
    popularidad = year_popularity_series['popularity']
    return (año, popularidad)