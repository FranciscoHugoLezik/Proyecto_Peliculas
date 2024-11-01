from typing import Tuple

import pandas as pd

from src.modules.credits.helpers.get_creditos import get_creditos
from src.modules.others.constants import MOVIES
from src.modules.credits.helpers.filtrar_con_retorno import filtrar_con_retorno


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
    
    
    sus_creditos = get_creditos(nombre, 
                                    'cast')
    sus_peliculas = pd.merge(sus_creditos, 
                             MOVIES, 
                             on='movie_id')
    con_retorno = filtrar_con_retorno(sus_peliculas)
    
    cantidad = len(sus_peliculas)
    cantidad_con_retorno = len(con_retorno)
    retorno_total = con_retorno['return'].sum().round(2)
    retorno_promedio = con_retorno['return'].mean().round(2)
    
    return(cantidad, 
           cantidad_con_retorno, 
           retorno_total, 
           retorno_promedio)