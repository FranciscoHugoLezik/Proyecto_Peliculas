from typing import Tuple

from src.modules.movies.helpers.get_filmacion import get_filmacion


def score_titulo(titulo: str) -> Tuple[str, 
                                       float]:
    """Se obtiene el año de estreno y la 
    popularidad de una pelicula.

    Args:
        titulo (str): es el titulo de una 
        pelicula.

    Returns:
        str: es el año de estreno.
        float: es la popularidad.
    """
    filmacion = get_filmacion(titulo)
    año = filmacion['release_year']
    popularidad = float(filmacion['popularity'].round(2))
    
    return (año, 
            popularidad)