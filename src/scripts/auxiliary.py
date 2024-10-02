if __name__ == "__main__":
    import constant as c
    from df_import import importar_archivo
else:
    from src.scripts import constant as c
    from src.scripts.df_import import importar_archivo


def get_meses():
    solo_meses = c.MOVIES['release_date'].dt.month
    return(solo_meses)


def get_numero_mes(mes):
    numero_de_mes = int(c.MESES.get(mes))
    return(numero_de_mes)


def get_dias():
    solo_dias = c.MOVIES['release_date'].dt.strftime('%A')
    return(solo_dias)


def get_dia_en_ingles(dia):
    dia_en_ingles = c.DIAS_EN_INGLES.get(dia)
    return(dia_en_ingles)


def get_filmacion(titulo):
    movies = c.MOVIES.copy()
    movies.set_index('title', 
                     inplace=True)
    filmación = movies.loc[titulo]
    return(filmación)


def get_movies_id(nombre, archivo):
    cast = importar_archivo('data', 
                            'ETL_data', 
                            'credits', 
                            f'{archivo}.parquet')
    actor = cast[cast['name'] == nombre]
    actor = actor[['name', 
                   'movie_id']].copy()
    actor.drop_duplicates(subset=['movie_id'], 
                          inplace=True)
    return(actor)


def get_peliculas(*columnas):
    peliculas = c.MOVIES[[*columnas]].copy()
    peliculas.rename(columns={'id': 'movie_id'}, 
                     inplace=True)
    return(peliculas)


def filtrar_por_retorno(peliculas_df):
    filtrado = peliculas_df[peliculas_df['return'] != 0]
    return(filtrado)


def procesar_peliculas(peliculas):
    peliculas.drop(columns=['movie_id', 
                            'name'], 
                            inplace=True)
    peliculas['release_date'] = peliculas['release_date'].dt.date
    peliculas['release_date'] = peliculas['release_date'].astype(str)
    peliculas.rename(columns={'title': 'Titulo', 
                              'release_date': 'Fecha_de_estreno', 
                              'return': 'Retorno', 
                              'budget': 'Presupuesto', 
                              'revenue': 'Ganancia'}, 
                     inplace=True)
    peliculas = peliculas.to_dict(orient="records")
    return(peliculas)