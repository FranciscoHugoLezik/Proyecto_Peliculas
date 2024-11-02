from typing import Tuple

from src.modules.movies.helpers.get_filmacion import get_filmacion


def votos_titulo(titulo: str) -> Tuple[int, 
                                       int, 
                                       float]:
    """Se obtiene el año de estreno, la 
    cantidad de votos y el promedio de 
    votos de una pelicula.

    Args:
        titulo (str): es el titulo de una 
        pelicula.

    Returns:
        int: es el año de estreno.
        int: es la cantidad de votos.
        float: es el promedio de votos.
    """
    filmacion = get_filmacion(titulo)
    titulo = filmacion['title']
    año = filmacion['release_year']
    cantidad = int(filmacion['vote_count'])
    promedio = float(filmacion['vote_average'])
    
    return (titulo, 
            año, 
            cantidad, 
            promedio)