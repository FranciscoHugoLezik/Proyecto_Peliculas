from typing import Tuple

if __name__ == "__main__":
    import movies_query_auxiliary as q
else:
    from src.scripts import movies_query_auxiliary as q


def cantidad_filmaciones_mes(mes: str) -> int:
    """Retorna la cantidad de filmaciones estrenadas en un 
    mes en particular, a lo largo de los años.

    Args:
        mes (str): Es un mes en español.

    Returns:
        cantidad (int): Es la cantidad de peliculas estrenadas.
    """
    meses = q.get_meses()
    cantidades = meses.value_counts()
    numero_mes = q.get_numero_mes(mes)
    cantidad = int(cantidades[numero_mes])
    
    return (cantidad)


def cantidad_filmaciones_dia(dia: str) -> int:
    """Retorna la cantidad de filmaciones estrenadas en un 
    dia en particular, a lo largo de los años.

    Args:
        dia (str): Es un dia en español.

    Returns:
        int: Es la cantidad de peliculas estrenadas.
    """
    dias = q.get_dias()
    cantidades = dias.value_counts()
    dia_en_ingles = q.get_dia_en_ingles(dia)
    cantidad = int(cantidades[dia_en_ingles])
    
    return (cantidad)


def score_titulo(titulo: str) -> Tuple[str, 
                                       float]:
    """Retorna el año en que fue estrenada una pelicula
    y su popularidad.

    Args:
        titulo (str): Es el titulo en ingles de una 
        pelicula.

    Returns:
        str: Es el año de estreno.
        float: Es la popularidad.
    """
    filmacion = q.get_filmacion(titulo)
    año = filmacion['release_year']
    popularidad = float(filmacion['popularity'])
    
    return (año, 
            popularidad)


def votos_titulo(titulo: str) -> Tuple[int, 
                                       int, 
                                       float]:
    """Retorna el año en que fue estrenada una pelicula
    la cantidad de votos y el promedio de votos.

    Args:
        titulo (str): Es el titulo en ingles de una 
        pelicula.

    Returns:
        int: Es el año de estreno.
        int: Es la cantidad de votos.
        float: Es el promedio de votos.
    """
    filmacion = q.get_filmacion(titulo)
    año = filmacion['release_year']
    cantidad = int(filmacion['vote_count'])
    promedio = float(filmacion['vote_average'])
    
    return (año, 
            cantidad, 
            promedio)