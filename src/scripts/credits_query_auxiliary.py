import sys
import os

if (__name__ == "__main__" 
    or "credits_query" in os.path.basename(sys.argv[0])):
    import constants as c
    from import_file import importar_archivo
else:
    from src.scripts import constants as c
    from src.scripts.import_file import importar_archivo


def get_movies_id(nombre, archivo):
    dataset = importar_archivo('data', 
                               'ETL_data', 
                               'credits', 
                               f'{archivo}.parquet')
    persona = dataset[dataset['name'] == nombre].copy()
    persona.drop_duplicates(subset=['movie_id'], 
                            inplace=True)
    return(persona)


def get_peliculas(*columnas):
    peliculas = c.MOVIES[[*columnas]].copy()
    peliculas.rename(columns={'id': 'movie_id'}, 
                     inplace=True)
    return(peliculas)


def filtrar_con_retorno(peliculas_df):
    filtrado = peliculas_df[peliculas_df['return'] != 0]
    return(filtrado)


def procesar_peliculas(peliculas):
    peliculas.drop(columns=['movie_id'], 
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