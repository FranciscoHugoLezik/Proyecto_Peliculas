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
    dia = dia.lower()
    dias_en_ingles = get_dias()
    cantidades = dias_en_ingles.value_counts()
    dia_en_ingles = get_dia_en_ingles(dia)
    
    cantidad = cantidades[dia_en_ingles]
    cantidad = int(cantidad)

    return (dia, cantidad)