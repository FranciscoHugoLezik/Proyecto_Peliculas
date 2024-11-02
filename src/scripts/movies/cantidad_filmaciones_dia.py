from fastapi import APIRouter

from src.modules.movies.functions.cantidad_filmaciones_dia \
    import cantidad_filmaciones_dia as calcular_cantidad


router = APIRouter()


@router.get("/cantidad_filmaciones_dia")
async def default_cantidad_filmaciones_dia() -> dict:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona un dia, en español, en la URL.
    
    Returns:
        dict: Es un texto con la explicacion del 
        proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": (
            "Retorna la cantidad de peliculas " 
            "que fueron estrenadas en un dia " 
            "escrito en español."),
        "Uso": (
            "Tenes que agregarle a esta URL " 
            "un dia en español. Por ejemplo: " 
            "/cantidad_filmaciones_dia/lunes")
    }
    return respuesta


@router.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str) -> dict:
    """Retorna la cantidad de filmaciones que 
    fueron estrenadas en el dia dado como argumento.
    
    Args: 
        dia (str): es un dia en español.
        
    Returns:
        dict: Es un texto con la 
        cantidad de filmaciones estrenadas en un dia 
        en particular.
    """
    cantidad = calcular_cantidad(dia)
    respuesta = {
        "Respuesta": 
            f'Fueron estrenadas {cantidad} películas en el día {dia}.'
    }
    return respuesta