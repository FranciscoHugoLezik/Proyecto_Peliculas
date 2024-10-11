import sys
import os
from typing import Tuple, List

import pandas as pd

import src.modules.constants as c
from src.modules.import_file import importar_archivo


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
    peliculas = peliculas[['title', 
                           'release_date', 
                           'return', 
                           'budget', 
                           'revenue']].copy()
    peliculas.rename(columns={'title': 'Titulo', 
                              'release_date': 'Fecha_de_estreno', 
                              'return': 'Retorno', 
                              'budget': 'Presupuesto', 
                              'revenue': 'Ganancia'}, 
                     inplace=True)
    peliculas['Fecha_de_estreno'] = peliculas['Fecha_de_estreno'].dt.date
    peliculas['Fecha_de_estreno'] = peliculas['Fecha_de_estreno'].astype(str)
    
    peliculas = peliculas.to_dict(orient="records")
    return(peliculas)