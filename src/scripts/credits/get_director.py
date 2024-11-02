from fastapi import APIRouter

from src.modules.credits.functions.get_director \
    import get_director as calcular_get_director


router = APIRouter()


@router.get("/get_director")
async def default_get_director() -> dict:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona el titulo de una filmacion 
    en la URL.
    
    Returns:
        HTMLResponse: es un texto con la explicacion 
        del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": """Retorna el nombre del director, el total 
                     de peliculas que dirigio, la cantidad que 
                     tiene datos de retorno y el total de retorno. 
                     Ademas retorna el titulo de cada pelicula, 
                     la fecha de estreno, el retorno individual, 
                     el costo y la ganancia.""",
        "Uso": """Tenes que agregarle a esta URL el 
               nombre de un director. La primera letra de cada 
               nombre y apellido debe estar en mayúscula y el 
               resto en minúscula. Por ejemplo: 
               /director/John Lasseter""", 
        "Algunos directores disponibles": (
            "John Lasseter", 
            "Joe Johnston", 
            "Howard Deutch", 
            "Forest Whitaker", 
            "Charles Shyer", 
            "Michael Mann", 
            "Sydney Pollack", 
            "Peter Hewitt", 
            "Peter Hyams", 
            "Martin Campbell"
        )
    }
    return respuesta


@router.get("/get_director/{nombre_director}")
async def get_director(nombre_director: str) -> dict:
    """Obtiene el nombre del director, el total 
    de peliculas que dirigio, la cantidad que 
    tiene retorno registrado y el total de retorno. 
    Ademas retorna el titulo de cada pelicula, 
    la fecha de estreno, el retorno individual, 
    el costo y la ganancia.
    
    Args:
        nombre (str): es el nombre de un director.
        
    Returns:
        HTMLResponse: es un texto con los resultados.
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