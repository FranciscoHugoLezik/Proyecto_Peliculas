import sys
import os
from typing import Tuple, List

import pandas as pd

if (__name__ == "__main__" 
    or "credits_query" in os.path.basename(sys.argv[0])):
    import constants as c
    from import_file import importar_archivo
else:
    from src.scripts import constants as c
    from src.scripts.import_file import importar_archivo


def get_creditos(persona: str, 
                 archivo: str) -> pd.DataFrame:
    """Importa un dataset guardado en la 
    carpeta credits (los creditos de las peliculas).
    Filtra los datos de la persona y elimina los 
    duplicados.

    Args:
        persona (str): es el nombre de una persona.
        archivo (str): es el nombre de un archivo.

    Returns:
        pd.DataFrame: contiene los creditos de la 
        persona.
    """
    dataset = importar_archivo('data', 
                               'ETL_data', 
                               'credits', 
                               f'{archivo}.parquet')
    sus_creditos = dataset[dataset['name'] == persona].copy()
    sus_creditos.drop_duplicates(subset=['movie_id'], 
                                 inplace=True)
    return(sus_creditos)


def get_columnas(*columnas: Tuple[str]) -> pd.DataFrame:
    """Selecciona unas columnas del dataframe 
    MOVIES.
    
    Args:
        *columnas (Tuple[str]): es una tupla del 
        nombre de una o mas columnas.

    Returns:
        pd.DataFrame: contiene las columnas 
        seleccionadas.
    """
    peliculas = c.MOVIES[[*columnas]].copy()
    return(peliculas)


def filtrar_con_retorno(peliculas: pd.DataFrame) -> pd.DataFrame:
    """Filtra las peliculas cuyo return es 
    mayor de cero.

    Args:
        peliculas (pd.DataFrame): cada fila es una 
        pelicula.

    Returns:
        pd.DataFrame: solo tiene peliculas que 
        cumplen con el filtro.
    """
    con_retorno = peliculas[peliculas['return'] > 0]
    return(con_retorno)


def procesar_peliculas(peliculas: pd.DataFrame) -> List[dict]:
    """Renombra las columnas y modifica los datos de 
    la columna 'Fecha_de_estreno'. Por último, lo 
    convierte en una lista de diccionarios.

    Args:
        peliculas (pd.DataFrame): cada fila es una 
        pelicula.

    Returns:
        list[dict]: cada diccionario es una pelicula.
    """
    peliculas_copia = peliculas.copy()
    peliculas_copia.rename(columns={'title': 'Titulo', 
                                    'release_date': 'Fecha_de_estreno', 
                                    'return': 'Retorno', 
                                    'budget': 'Presupuesto', 
                                    'revenue': 'Ganancia'}, 
                           inplace=True)
    
    peliculas_copia['Fecha_de_estreno'] = peliculas_copia['Fecha_de_estreno'].dt.date
    peliculas_copia['Fecha_de_estreno'] = peliculas_copia['Fecha_de_estreno'].astype(str)
    
    peliculas = peliculas_copia.to_dict(orient="records")
    return(peliculas)