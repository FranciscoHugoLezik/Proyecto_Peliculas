from fastapi import APIRouter

from src.modules.movies.functions.cantidad_filmaciones_mes \
    import cantidad_filmaciones_mes as calcular_cantidad


router = APIRouter()


@router.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str) -> dict:
    """Retorna la cantidad acumulada de filmaciones 
    que fueron estrenadas en un determinado mes, 
    a lo largo del tiempo.
    
    Arg: 
        
    mes (str): es un mes en español.
        
    Return:
     
    dict: es un texto con la respuesta.
    """
    mes, cantidad = calcular_cantidad(mes)
    respuesta = {
        "Respuesta": 
            f'Fueron estrenadas {cantidad} filmaciones en el mes de {mes}.'
    }
    return respuesta