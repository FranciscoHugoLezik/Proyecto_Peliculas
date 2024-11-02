from src.modules.others.constants import MESES


def get_numero_del_mes(mes: str) -> int:
    """Se obtiene el numero del mes 
    solicitado.

    Args:
        mes (str): es un mes en español.

    Returns:
        int: es el numero del mes.
    """
    mes = mes.lower()
    numero_del_mes = MESES.get(mes)
    numero_del_mes = int(numero_del_mes)
    
    return(numero_del_mes)