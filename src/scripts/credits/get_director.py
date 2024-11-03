from fastapi import APIRouter

from src.modules.credits.functions.get_director \
    import get_director as calcular_get_director


router = APIRouter()


@router.get("/get_director/{nombre_director}")
async def get_director(nombre_director: str) -> dict:
    """Retorna el nombre del director, el cantidad de 
    filmaciones que dirigió, la cantidad de filmaciones 
    que tienen datos de retorno y el retorno total de 
    sus filmaciones. 
    Ademas retorna los datos de las filmaciones con 
    datos de retorno. Los datos retornados son el título 
    de cada filmación, su fecha de estreno, su retorno 
    individual, su costo y su ganancia.
    
    Arg:
    
    nombre (str): es el nombre de un director.
        
    Return:
    
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
            f'ha dirigido {total_peliculas} filmaciones. '
            f'Hay {total_con_retorno} filmaciones con '
            f'retorno registrado. '
            f'El retorno total es {total_retorno}.' 
            ), 
        "Las filmaciones con retorno son": peliculas
        }
    return respuesta