import pandas as pd

from src.modules.movies.helpers.get_meses import get_meses
from src.modules.movies.helpers.get_numero_mes import get_numero_mes


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
    meses = get_meses()
    cantidades = meses.value_counts()
    numero_mes = get_numero_mes(mes)
    cantidad = int(cantidades[numero_mes])
    
    return (cantidad)