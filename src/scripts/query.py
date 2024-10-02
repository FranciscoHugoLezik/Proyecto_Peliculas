import pandas as pd

if __name__ == "__main__":
    import constant as c
    import auxiliary as aux
else:
    from src.scripts import constant as c
    from src.scripts import auxiliary as aux


def cantidad_filmaciones_mes(mes):
    solo_meses = c.MOVIES['release_date'].dt.month
    cantidad_por_mes = solo_meses.value_counts()
    
    mes = int(c.MESES.get(mes))
    
    cantidad = int(cantidad_por_mes[mes])
    
    return (cantidad)


def cantidad_filmaciones_dia(dia):
    solo_dias = c.MOVIES['release_date'].dt.strftime('%A')
    cantidad_por_dia = solo_dias.value_counts()
    
    dia = c.DIAS.get(dia)
    
    cantidad = int(cantidad_por_dia[dia])
    
    return (cantidad)


def score_titulo(titulo):
    movies = c.MOVIES.copy()
    movies.set_index('title', 
                     inplace=True)
    filmación = movies.loc[titulo]
    
    año = int(filmación['release_year'])
    popularidad = float(filmación['popularity'])
    
    return (año, 
            popularidad)


def votos_titulo(titulo): 
    movies = c.MOVIES.copy()
    movies.set_index('title', 
                     inplace=True)
    filmación = movies.loc[titulo]
    
    año = int(filmación['release_year'])
    cantidad = int(filmación['vote_count'])
    promedio = float(filmación['vote_average'])
    
    return (año, 
            cantidad, 
            promedio)


def get_actor(nombre_actor):
    cast = aux.importar_archivo('data', 
                                'ETL_data', 
                                'credits', 
                                'cast.parquet')
    
    actor = cast[cast['name'] == nombre_actor]
    actor = actor[['name', 
                   'movie_id']].copy()
    actor.drop_duplicates(subset=['movie_id'], 
                          inplace=True)
    
    cantidad = len(actor['movie_id'])
    
    peliculas = c.MOVIES[['id', 
                          'return']].copy()
    peliculas.rename(columns={'id': 'movie_id'}, 
                     inplace=True)
    peliculas = pd.merge(actor, 
                         peliculas, 
                         on='movie_id')
    
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
    crew = aux.importar_archivo('data', 
                                'ETL_data', 
                                'credits', 
                                'crew.parquet')
    
    director = crew[crew['job'] == 'Director']
    director = director[director['name'] == nombre_director]
    director = director[['name', 
                         'movie_id']].copy()
    
    cantidad = len(director['movie_id'])
    
    peliculas = c.MOVIES[['id', 
                          'title', 
                          'release_date', 
                          'return', 
                          'budget', 
                          'revenue']].copy()
    peliculas.rename(columns={'id': 'movie_id'}, 
                     inplace=True)
    peliculas = pd.merge(director, 
                         peliculas, 
                         on='movie_id')
    
    peliculas = peliculas[peliculas['return'] != 0]
    
    cantidad_con_retorno = len(peliculas['movie_id'])
    
    total = peliculas['return'].sum()
    total = round(total, 2)
    
    peliculas.drop(columns=['movie_id', 
                            'name'], inplace=True)

    
    peliculas['release_date'] = peliculas['release_date'].dt.date
    peliculas['release_date'] = peliculas['release_date'].astype(str)

    peliculas.rename(columns={'title': 'Titulo', 
                              'release_date': 'Fecha_de_estreno', 
                              'return': 'Retorno', 
                              'budget': 'Presupuesto', 
                              'revenue': 'Ganancia'}, 
                     inplace=True)
    
    peliculas_dict = peliculas.to_dict(orient="records")
    
    return (cantidad, 
            cantidad_con_retorno, 
            total, 
            peliculas_dict)