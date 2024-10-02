import pandas as pd

if __name__ == "__main__":
    from df_import import importar_archivo
    import constant as c
else:
    from src.scripts.df_import import importar_archivo


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