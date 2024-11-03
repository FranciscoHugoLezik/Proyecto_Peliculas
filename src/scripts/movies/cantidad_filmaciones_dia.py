from fastapi import APIRouter

from src.modules.movies.functions.cantidad_filmaciones_dia \
    import cantidad_filmaciones_dia as calcular_cantidad


router = APIRouter()


@router.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str) -> dict:
    """Retorna la cantidad de filmaciones que 
    fueron estrenadas en el dia dado como argumento.
    
    Arg: \n
        dia (str): es un dia en español.
        
    Return: \n
        dict: es un texto con la 
        cantidad de filmaciones estrenadas en un dia 
        en particular.
    """
    dia, cantidad = calcular_cantidad(dia)
    respuesta = {
        "Respuesta": 
            f'Fueron estrenadas {cantidad} películas en el día {dia}.'
    }
    return respuesta