import os

import pandas as pd


def importar_archivo(*args):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(current_dir))
    file_path = os.path.join(base_dir, *args)
    archivo = pd.read_parquet(file_path, 
                              engine='fastparquet')
    return(archivo)


movies = importar_archivo('data', 
                          'ETL_data', 
                          'movies_dataset', 
                          'movies.parquet')
movies.set_index('title', 
                 inplace=True)


def cantidad_filmaciones_mes(mes):
    solo_meses = movies['release_date'].dt.month
    cantidad_por_mes = solo_meses.value_counts()
    
    meses = {
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
    mes = int(meses.get(mes))
    
    cantidad = int(cantidad_por_mes[mes])
    
    return (cantidad)


def cantidad_filmaciones_dia(dia):
    solo_dias = movies['release_date'].dt.strftime('%A')
    cantidad_por_dia = solo_dias.value_counts()
    
    dias = {
        'lunes': 'Monday', 
        'martes': 'Tuesday', 
        'miercoles': 'Wednesday', 
        'jueves': 'Thursday', 
        'viernes': 'Friday', 
        'sabado': 'Saturday', 
        'domingo': 'Sunday'
    }
    dia = dias.get(dia)
    
    cantidad = int(cantidad_por_dia[dia])
    
    return (cantidad)


def score_titulo(titulo_de_la_filmación):
    filmación = movies.loc[titulo_de_la_filmación]
    
    año = int(filmación['release_year'])
    popularidad = float(filmación['popularity'])
    
    return (año, popularidad)


def votos_titulo(titulo_de_la_filmación): 
    filmación = movies.loc[titulo_de_la_filmación]
    
    año = int(filmación['release_year'])
    cantidad_de_votos = int(filmación['vote_count'])
    promedio_de_votos = float(filmación['vote_average'])
    
    return (año, cantidad_de_votos, promedio_de_votos)


def get_actor(nombre_actor):
    cast = importar_archivo('data', 
                            'ETL_data', 
                            'credits', 
                            'cast.parquet')
    
    actor = cast[cast['name'] == nombre_actor]
    actor = actor[['name', 'movie_id']].copy()
    actor.drop_duplicates(subset=['movie_id'], inplace=True)
    
    cantidad = len(actor)
    
    peliculas = movies[['id', 'return']].copy()
    peliculas.rename(columns={'id': 'movie_id'}, inplace=True)
    peliculas = pd.merge(actor, peliculas, on='movie_id')
    
    peliculas_con_retorno = peliculas[peliculas['return'] != 0]
    
    cantidad_con_retorno = len(peliculas_con_retorno)
    
    total = peliculas_con_retorno['return'].sum()
    total = round(total, 2)
    
    promedio = peliculas_con_retorno['return'].mean()
    promedio = round(promedio, 2)
    
    return(cantidad, 
           cantidad_con_retorno, 
           total, 
           promedio)


def get_director(nombre_director):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(current_dir))
    file_path = os.path.join(base_dir, 'data', 'credits', 'crew_ETL.parquet')

    crew_df = pd.read_parquet(file_path, engine='fastparquet')
    
    name_job_movieId = crew_df[['name', 'job', 'movie_id']]
    name_job_movieId = name_job_movieId[name_job_movieId['job'] == 'Director']
    nombreDirector_movieId = name_job_movieId[name_job_movieId['name'] == nombre_director]
    cantidad_peliculas = len(nombreDirector_movieId['movie_id'])
    movieId_title_dateRelease_return_budget_revenue = pd.DataFrame(movies[['id','title','release_date','return','budget','revenue']])
    movieId_title_dateRelease_return_budget_revenue.rename(columns={'id': 'movie_id'}, inplace=True)
    nombreDirector_peliculas = pd.merge(nombreDirector_movieId, movieId_title_dateRelease_return_budget_revenue)
    nombreDirector_peliculas = pd.DataFrame(nombreDirector_peliculas[nombreDirector_peliculas['return'] != 0])
    cantidad_peliculas_con_retorno = len(nombreDirector_peliculas['movie_id'])
    nombreDirector_peliculas.drop(columns=["movie_id","name","job"], inplace=True)
    nombreDirector_peliculas.reset_index(drop=True, inplace=True)
    total_retorno = nombreDirector_peliculas["return"].sum()
    nombreDirector_peliculas['release_date'] = nombreDirector_peliculas['release_date'].dt.date
    nombreDirector_peliculas['release_date'] = nombreDirector_peliculas['release_date'].astype(str)
    nombreDirector_peliculas.rename(columns={'title': 'Titulo'}, inplace=True)
    nombreDirector_peliculas.rename(columns={'release_date': 'Fecha_de_estreno'}, inplace=True)
    nombreDirector_peliculas.rename(columns={'return': 'Retorno'}, inplace=True)
    nombreDirector_peliculas.rename(columns={'budget': 'Presupuesto'}, inplace=True)
    nombreDirector_peliculas.rename(columns={'revenue': 'Ganancia'}, inplace=True)
    peliculas_dict = nombreDirector_peliculas.to_dict(orient="records")
    return (cantidad_peliculas, cantidad_peliculas_con_retorno, total_retorno, peliculas_dict)