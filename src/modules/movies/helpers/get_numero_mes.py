from src.modules.others.constants import MESES


def get_numero_mes(mes: str) -> int:
    """Se obtiene el numero del mes 
    solicitado.

    Args:
        mes (str): es un mes en español.

    Returns:
        int: es el numero del mes.
    """
    numero_de_mes = int(MESES.get(mes))
    
    return(numero_de_mes)