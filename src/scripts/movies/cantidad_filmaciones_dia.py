from fastapi import APIRouter

from src.modules.movies.functions.cantidad_filmaciones_dia \
    import cantidad_filmaciones_dia as calcular_cantidad


router = APIRouter()


@router.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str) -> dict:
    """Retorna la cantidad acumulada de filmaciones 
    que fueron estrenadas en un determinado día, 
    a lo largo del tiempo.
    
    Arg:
    
    dia (str): es un dia en español.
        
    Return:
        
    dict: es un texto con la respuesta.
    """
    dia, cantidad = calcular_cantidad(dia)
    respuesta = {
        "Respuesta": 
            f'Fueron estrenadas {cantidad} filmaciones en el día {dia}.'
    }
    return respuesta