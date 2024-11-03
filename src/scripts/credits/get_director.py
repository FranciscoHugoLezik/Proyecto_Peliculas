from fastapi import APIRouter

from src.modules.credits.functions.get_director \
    import get_director as calcular_get_director


router = APIRouter()


@router.get("/get_director/{nombre_director}")
async def get_director(nombre_director: str) -> dict:
    """Obtiene el nombre del director, el total 
    de peliculas que dirigio, la cantidad que 
    tiene retorno registrado y el total de retorno. 
    Ademas retorna el titulo de cada pelicula, 
    la fecha de estreno, el retorno individual, 
    el costo y la ganancia.
    
    Arg: \n
        nombre (str): es el nombre de un director.
        
    Return: \n
        dict: es un texto con los resultados.
        
    Algunos directores disponibles: \n
        John Lasseter 
        Joe Johnston 
        Howard Deutch 
        Forest Whitaker 
        Charles Shyer 
        Michael Mann 
        Sydney Pollack 
        Peter Hewitt 
        Peter Hyams 
        Martin Campbell
    """
    (nombre, 
     total_peliculas, 
     total_con_retorno, 
     total_retorno, 
     peliculas) = calcular_get_director(nombre_director)
    
    respuesta = {
        "Director": (
            f'El director {nombre} '
            f'ha dirigido {total_peliculas} peliculas. '
            f'Hay {total_con_retorno} peliculas con '
            f'retorno registrado. '
            f'El retorno total es {total_retorno}.' 
            ), 
        "Peliculas_con_retorno": (
            "Las peliculas, con retorno "  
            "registrado, son las siguientes: "
            ), 
        "Peliculas": peliculas
        }
    return respuesta