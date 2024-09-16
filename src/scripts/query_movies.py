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
    title_year_popularity_df = pd.DataFrame(movies_df[['title',
                                                       'release_year',
                                                       'popularity']])
    title_year_popularity_df.set_index('title', inplace=True)
    year_popularity_series = title_year_popularity_df.loc[titulo_de_la_filmación]
    año = year_popularity_series['release_year']
    año = int(año)
    popularidad = year_popularity_series['popularity']
    return (año, popularidad)


def votos_titulo(titulo_de_la_filmación):
    title_year_count_average_df = pd.DataFrame(movies_df[['title',
                                                          'release_year',
                                                          'vote_count',
                                                          'vote_average']])
    title_year_count_average_df.set_index('title', inplace=True)
    title_year_count_average_series = title_year_count_average_df.loc[titulo_de_la_filmación]
    año = title_year_count_average_series['release_year']
    año = int(año)
    cantidad_de_votos = title_year_count_average_series['vote_count']
    promedio_de_votos = title_year_count_average_series['vote_average']
    return (año, cantidad_de_votos, promedio_de_votos)


def get_actor(nombre_actor):
    
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(current_dir))
    file_path = os.path.join(base_dir, 'data', 'credits', 'cast_ETL.parquet')

    cast_df = pd.read_parquet(file_path, engine='fastparquet')
    
    
    name_movieId = cast_df[['name', 'movie_id']]
    nombreActor_movieId = name_movieId[name_movieId['name'] == nombre_actor]
    nombreActor_movieId = nombreActor_movieId.drop_duplicates(subset=['movie_id'])
    cantidad_peliculas = len(nombreActor_movieId['movie_id'])
    movieId_title_return = pd.DataFrame(movies_df[['id','title','return']])
    movieId_title_return.rename(columns={'id': 'movie_id'}, inplace=True)
    nombreActor_peliculas = pd.merge(nombreActor_movieId, movieId_title_return)
    nombreActor_peliculas = nombreActor_peliculas[nombreActor_peliculas['return'] != 0]
    nombreActor_peliculas.reset_index(inplace=True)
    cantidad_peliculas_con_retorno = len(nombreActor_peliculas['movie_id'])
    total_retorno = nombreActor_peliculas["return"].sum()
    total_retorno = round(total_retorno, 2)
    promedio_retorno = nombreActor_peliculas["return"].mean()
    promedio_retorno = round(promedio_retorno, 2)
    return (cantidad_peliculas, cantidad_peliculas_con_retorno, total_retorno, promedio_retorno)


def get_director(nombre_director):
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(current_dir))
    file_path = os.path.join(base_dir, 'data', 'credits', 'crew_ETL.parquet')

    crew_df = pd.read_parquet(file_path, engine='fastparquet')
    
    name_job_movieId = crew_df[['name', 'job', 'movie_id']]
    name_job_movieId = name_job_movieId[name_job_movieId['job'] == 'Director']
    nombreDirector_movieId = name_job_movieId[name_job_movieId['name'] == nombre_director]
    cantidad_peliculas = len(nombreDirector_movieId['movie_id'])
    movieId_title_dateRelease_return_budget_revenue = pd.DataFrame(movies_df[['id','title','release_date','return','budget','revenue']])
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