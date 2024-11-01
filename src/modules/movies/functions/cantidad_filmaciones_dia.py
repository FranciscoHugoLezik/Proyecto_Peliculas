from src.modules.movies.helpers.get_dias import get_dias
from src.modules.movies.helpers.get_dia_en_ingles import get_dia_en_ingles


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
    dias = get_dias()
    cantidades = dias.value_counts()
    dia_en_ingles = get_dia_en_ingles(dia)
    cantidad = int(cantidades[dia_en_ingles])
    
    return (cantidad)