from src.modules.others.constants import DIAS_EN_INGLES


def get_dia_en_ingles(dia: str) -> str:
    """Se obtiene el dia en ingles del dia 
    solicitado.

    Args:
        dia (str): es un dia en español.

    Returns:
        str: es el dia en ingles.
    """
    dia_en_ingles = DIAS_EN_INGLES.get(dia)
    
    return(dia_en_ingles)