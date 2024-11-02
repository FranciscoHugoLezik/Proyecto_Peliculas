import pandas as pd

from src.modules.others.constants import MOVIES


def get_filmacion(titulo: str) -> pd.Series:
    """Selecciona una pelicula.

    Args:
        titulo (str): es el titulo de la 
        pelicula.

    Returns:
        pd.Series: son los datos de la 
        pelicula.
    """
    titulo = titulo.lower()
    movies = MOVIES.copy()
    filmacion = movies[
        movies['title'].str.lower() == titulo
        ].copy()
    filmacion = filmacion.squeeze()
    
    return(filmacion)