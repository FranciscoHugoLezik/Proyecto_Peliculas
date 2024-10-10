import sys
import os

import pandas as pd

if (__name__ == "__main__" 
    or "movies_query" in os.path.basename(sys.argv[0])):
    import constants as c
else:
    from src.scripts import constants as c
    

def get_meses() -> pd.Series:
    """Se obtienen los numeros de los meses de 
    la columna 'release date' (fecha de estreno) 
    del dataset MOVIES.

    Returns:
        pd.Series: son los numeros de los meses.
    """
    solo_meses = c.MOVIES['release_date'].dt.month
    
    return(solo_meses)


def get_numero_mes(mes: str) -> int:
    """Se obtiene el numero del mes 
    solicitado.

    Args:
        mes (str): es un mes en español.

    Returns:
        int: es el numero del mes.
    """
    numero_de_mes = int(c.MESES.get(mes))
    
    return(numero_de_mes)


def get_dias() -> pd.Series:
    """Se obtienen los dias en ingles de la 
    columna 'release date' (fecha de estreno) 
    del dataset MOVIES.

    Returns:
        pd.Series: son los dias en ingles.
    """
    solo_dias = c.MOVIES['release_date'].dt.strftime('%A')
    
    return(solo_dias)


def get_dia_en_ingles(dia: str) -> str:
    """Se obtiene el dia en ingles del dia 
    solicitado.

    Args:
        dia (str): es un dia en español.

    Returns:
        str: es el dia en ingles.
    """
    dia_en_ingles = c.DIAS_EN_INGLES.get(dia)
    
    return(dia_en_ingles)


def get_filmacion(titulo: str) -> pd.Series:
    """Selecciona una pelicula.

    Args:
        titulo (str): es el titulo de la 
        pelicula.

    Returns:
        pd.Series: son los datos de la 
        pelicula.
    """
    movies = c.MOVIES.copy()
    filmacion = movies[movies['title'] == titulo].copy()
    filmacion = filmacion.squeeze()
    
    return(filmacion)