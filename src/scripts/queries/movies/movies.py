from typing import Tuple

if __name__ == "__main__":
    import auxiliary as q
else:
    from src.scripts.movies_query import auxiliary as q
    
print('Todo bien')


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
    meses = q.get_meses()
    cantidades = meses.value_counts()
    numero_mes = q.get_numero_mes(mes)
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
    dias = q.get_dias()
    cantidades = dias.value_counts()
    dia_en_ingles = q.get_dia_en_ingles(dia)
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
    filmacion = q.get_filmacion(titulo)
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
    filmacion = q.get_filmacion(titulo)
    año = int(filmacion['release_year'])
    cantidad = int(filmacion['vote_count'])
    promedio = float(filmacion['vote_average'])
    
    return (año, 
            cantidad, 
            promedio)