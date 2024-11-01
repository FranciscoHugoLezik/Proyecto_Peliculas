from typing import Tuple, List

import pandas as pd

from src.modules.credits.helpers.get_creditos import get_creditos
from src.modules.others.constants import MOVIES
from src.modules.credits.helpers.filtrar_con_retorno import filtrar_con_retorno
from src.modules.credits.helpers.procesar_peliculas import procesar_peliculas


def get_director(nombre: str) -> Tuple[int, 
                                       int, 
                                       float, 
                                       List[dict]]:
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
    
    sus_creditos = get_creditos(nombre, 
                                    'crew')
    sus_creditos = sus_creditos.query('job == "Director"')
    movies_id = sus_creditos['movie_id'].copy()
    sus_peliculas = pd.merge(movies_id, 
                             MOVIES, 
                             on='movie_id')
    peliculas_con_retorno = filtrar_con_retorno(sus_peliculas)
    
    cantidad = len(sus_peliculas)
    cantidad_con_retorno = len(peliculas_con_retorno)
    retorno_total = peliculas_con_retorno['return'].sum().round(2)
    peliculas_con_retorno = procesar_peliculas(peliculas_con_retorno)
    
    return (cantidad, 
            cantidad_con_retorno, 
            retorno_total, 
            peliculas_con_retorno)


