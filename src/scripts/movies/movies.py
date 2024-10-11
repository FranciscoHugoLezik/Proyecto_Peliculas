from typing import Tuple

import src.scripts.movies.auxiliary_movies as aux


def cantidad_filmaciones_mes(mes: str) -> int:
    """Se obtiene la cantidad de estrenos de 
    filmaciones de cada mes del año, a lo largo 
    de los años, y se selecciona la cantidad 
    del mes pedido.

    Args:
        mes (pd.Series): es un mes en español.

    Returns:
        int: es la cantidad de peliculas 
        estrenadas en el mes pedido.
    """
    meses = aux.get_meses()
    cantidades = meses.value_counts()
    numero_mes = aux.get_numero_mes(mes)
    cantidad = int(cantidades[numero_mes])
    
    return (cantidad)


def cantidad_filmaciones_dia(dia: str) -> int:
    """Se obtiene la cantidad de estrenos de las 
    filmaciones de cada dia de la semana, a lo 
    largo de los años, y se selecciona la 
    cantidad del dia pedido.

    Args:
        dia (str): es un dia en español.

    Returns:
        int: es la cantidad de peliculas 
        estrenadas en el dia pedido.
    """
    dias = aux.get_dias()
    cantidades = dias.value_counts()
    dia_en_ingles = aux.get_dia_en_ingles(dia)
    cantidad = int(cantidades[dia_en_ingles])
    
    return (cantidad)


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
    filmacion = aux.get_filmacion(titulo)
    año = int(filmacion['release_year'])
    popularidad = float(filmacion['popularity'].round(2))
    
    return (año, 
            popularidad)


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
    filmacion = aux.get_filmacion(titulo)
    año = int(filmacion['release_year'])
    cantidad = int(filmacion['vote_count'])
    promedio = float(filmacion['vote_average'])
    
    return (año, 
            cantidad, 
            promedio)