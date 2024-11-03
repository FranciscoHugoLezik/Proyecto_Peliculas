import pandas as pd

from src.modules.movies.helpers.get_meses import get_meses
from src.modules.movies.helpers.get_numero_del_mes import get_numero_del_mes


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
    mes = mes.lower()
    numeros_de_los_meses = get_meses()
    cantidades = numeros_de_los_meses.value_counts()
    numero_del_mes = get_numero_del_mes(mes)
    
    cantidad = cantidades[numero_del_mes]
    cantidad = int(cantidad)
    
    return (mes, cantidad)