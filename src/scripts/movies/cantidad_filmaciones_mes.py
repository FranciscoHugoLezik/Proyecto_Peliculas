from fastapi import APIRouter

from src.modules.movies.functions.cantidad_filmaciones_mes \
    import cantidad_filmaciones_mes as calcular_cantidad


router = APIRouter()


@router.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str) -> dict:
    """Retorna la cantidad de filmaciones que 
    fueron estrenadas en un determinado mes.
    
    Arg: \n
        mes (str): es un mes en español.
        
    Return: \n
        dict: es un texto con la cantidad de 
        filmaciones estrenadas en un mes 
        en particular.
    """
    mes, cantidad = calcular_cantidad(mes)
    respuesta = {
        "Respuesta": 
            f'Fueron estrenadas {cantidad} películas en el mes de {mes}.'
    }
    return respuesta