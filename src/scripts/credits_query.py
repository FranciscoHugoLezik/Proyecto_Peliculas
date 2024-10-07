from typing import Tuple

import pandas as pd

if __name__ == "__main__":
    import credits_query_auxiliary as q
else:
    from src.scripts import credits_query_auxiliary as q


def get_actor(nombre: str) -> Tuple[int, 
                                    int, 
                                    float, 
                                    float]:
    """Selecciona las peliculas en las que 
    participo el actor y las peliculas que 
    tienen retorno registrado. Calcula la 
    cantidad de peliculas, la cantidad con 
    retorno, la sumatoria de la columna 
    'return' y el promedio, tambien de la 
    columna 'return'.

    Args:
        nombre (str): es el nombre de un actor.

    Returns:
        Tuple[int, int, float, float]: Son, de primero 
        a último, la cantidad de peliculas en las que 
        participo, la cantidad de peliculas con retorno, 
        el retorno total y el retorno promedio.
    """
    sus_creditos = q.get_creditos(nombre, 
                                  'cast')
    peliculas = q.get_columnas('movie_id', 
                              'return')
    sus_peliculas = pd.merge(sus_creditos, 
                             peliculas, 
                             on='movie_id')
    con_retorno = q.filtrar_con_retorno(sus_peliculas)
    
    cantidad = len(sus_peliculas)
    cantidad_con_retorno = len(con_retorno)
    retorno_total = con_retorno['return'].sum().round(2)
    retorno_promedio = con_retorno['return'].mean().round(2)
    
    return(cantidad, 
           cantidad_con_retorno, 
           retorno_total, 
           retorno_promedio)


def get_director(nombre: str) -> Tuple[int, 
                                       int, 
                                       float, 
                                       list[dict]]:
    """Selecciona las peliculas que dirigio 
    el director y las peliculas que tienen 
    retorno registrado. Calcula la cantidad 
    de peliculas, la cantidad con retorno y 
    la sumatoria de la columna 'return'.

    Args:
        nombre (str): es el nombre del director.

    Returns:
        Tuple[int, int, float, list[dict]]: Son, del 
        primero al ultimo, la cantidad de peliculas 
        que dirigio, la cantidad de peliculas con retorno, 
        el retorno total y los datos de las peliculas 
        (el titulo, la fecha de estreno, el retorno, 
        el presupuesto y el ingreso)
    """
    sus_creditos = q.get_creditos(nombre, 
                                  'crew')
    sus_creditos = sus_creditos.query('job == "Director"')
    sus_creditos = sus_creditos['movie_id'].copy()
    peliculas = q.get_columnas('movie_id', 
                               'title', 
                               'release_date', 
                               'return', 
                               'budget', 
                               'revenue')
    sus_peliculas = pd.merge(sus_creditos, 
                             peliculas, 
                             on='movie_id')
    peliculas_con_retorno = q.filtrar_con_retorno(sus_peliculas)
    
    cantidad = len(sus_peliculas)
    cantidad_con_retorno = len(peliculas_con_retorno)
    retorno_total = peliculas_con_retorno['return'].sum().round(2)
    peliculas_con_retorno = q.procesar_peliculas(peliculas_con_retorno)
    
    return (cantidad, 
            cantidad_con_retorno, 
            retorno_total, 
            peliculas_con_retorno)