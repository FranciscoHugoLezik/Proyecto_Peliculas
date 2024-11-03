from fastapi import APIRouter

from src.modules.credits.functions.get_actor \
    import get_actor as calcular_get_actor


router = APIRouter()


@router.get("/get_actor/{nombre_actor}")
async def get_actor(nombre_actor: str) -> dict:
    """Retorna el nombre del actor, la cantidad de 
    filmaciones en las que participó, la cantidad de
    filmaciones que tienen datos de retorno, el 
    retorno total de sus filmaciones y el retorno 
    promedio de sus filmaciones.
    
    Arg:
    
    nombre (str): es el nombre de un actor.
        
    Return:
    
    dict: es un texto con los resultados.
        
    Algunos actores disponibles: \n
        Tom Hanks 
        Tim Allen 
        Don Rickles 
        Jim Varney 
        Wallace Shawn 
        John Ratzenberger 
        Annie Potts 
        John Morris 
        Erik von Detten 
        Laurie Metcalf
    """
    (nombre, 
     total_peliculas, 
     total_con_retorno, 
     total_retorno,
     promedio_retorno) = calcular_get_actor(nombre_actor)
    
    respuesta = {
        "Respuesta": (
            f'El actor {nombre} '
            f'ha participado en {total_peliculas} ' 
            f'filmaciones. ' 
            f'Hay {total_con_retorno} filmaciones ' 
            f'con datos de retorno. '
            f'El actor logró un retorno total de ' 
            f'{total_retorno} ' 
            f'y su promedio es de {promedio_retorno} ' 
            f'por filmación.'
            )
        }
    return respuesta