from fastapi import APIRouter

from src.modules.movies.functions.cantidad_filmaciones_mes \
    import cantidad_filmaciones_mes as calcular_cantidad


router = APIRouter()


@router.get("/cantidad_filmaciones_mes")
async def default_cantidad_filmaciones_mes() -> dict:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona un mes, en español, en la URL.
    
    Returns:
        dict: es un texto con la explicacion del 
        proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": (
            "Retorna la cantidad de peliculas " 
            "que fueron estrenadas en un mes " 
            "escrito en español."),
        "Uso": (
            "Tenes que agregarle a esta URL " 
            "un mes en español. Por ejemplo: " 
            "/cantidad_filmaciones_mes/enero")
    }
    return respuesta


@router.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str) -> dict:
    """Retorna la cantidad de filmaciones que 
    fueron estrenadas en un determinado mes.
    
    Args: 
        mes (str): es un mes en español.
        
    Returns:
        dict: Es un texto con la cantidad de 
        filmaciones estrenadas en un mes 
        en particular.
    """
    cantidad = calcular_cantidad(mes)
    respuesta = {
        "Respuesta": 
            f'Fueron estrenadas {cantidad} películas en el mes de {mes}.'
    }
    return respuesta