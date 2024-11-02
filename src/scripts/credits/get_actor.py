from fastapi import APIRouter

from src.modules.credits.functions.get_actor \
    import get_actor as calcular_get_actor


router = APIRouter()


@router.get("/get_actor")
async def default_get_actor() -> dict:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona el titulo de una filmacion 
    en la URL.
    
    Returns:
        dict: es un texto con la explicacion 
        del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": (
            "Retorna el nombre del actor, "
            "el total de peliculas en las que "
            "participo, la cantidad que tiene "
            "datos de retorno, el total de retorno "
            "y su promedio."
            ), 
        "Uso": (
            "Tenes que agregarle a esta URL "
            "el nombre de un actor. La primera letra "
            "de cada nombre y apellido debe estar "
            "en mayúscula y el resto en minúscula. "
            "Por ejemplo: /actor/Tom Hanks"
            ), 
        "Algunos actores disponibles": (
            "Tom Hanks", 
            "Tim Allen", 
            "Don Rickles", 
            "Jim Varney", 
            "Wallace Shawn", 
            "John Ratzenberger", 
            "Annie Potts", 
            "John Morris", 
            "Erik von Detten", 
            "Laurie Metcalf"
        )
    }
    return respuesta


@router.get("/get_actor/{nombre_actor}")
async def get_actor(nombre_actor: str) -> dict:
    """Obtiene el nombre del actor, la cantidad de 
    peliculas en las que participo, la cantidad 
    que tiene datos de retorno, el total de 
    retorno y su promedio.
    
    Args:
        nombre (str): es el nombre de un actor.
        
    Returns:
        dict: es un texto con los resultados.
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
            f'peliculas. ' 
            f'Hay {total_con_retorno} peliculas ' 
            f'con datos de retorno. '
            f'El actor logró un retorno total de ' 
            f'{total_retorno} ' 
            f'y su promedio es de {promedio_retorno} ' 
            f'por pelicula.'
            )
        }
    return respuesta