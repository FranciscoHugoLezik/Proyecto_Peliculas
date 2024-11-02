from fastapi import APIRouter

from src.modules.movies.functions.votos_titulo \
    import votos_titulo as calcular_votos


router = APIRouter()


@router.get("/votos_titulo")
async def default_votos_titulo() -> dict:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona el titulo de una filmacion 
    en la URL.
    
    Returns:
        dict: es un texto con la explicacion 
        del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": (
            "Retorna el titulo, el año, la cantidad "
            "de votos y el promedio de votos de una "
            "pelicula. Si la cantidad de votos es menor "
            "a 2000 no devuelve ningun valor."
            ), 
        "Uso": (
            "Tenes que agregarle a esta URL "
            "el titulo de una pelicula. "
            "Por ejemplo: /votos_titulo/Toy Story"
            ), 
        "Algunos títulos disponibles": [
            "Toy Story", 
            "Jumanji", 
            "Grumpier Old Men", 
            "Waiting to Exhale", 
            "Father of the Bride Part II", 
            "Heat", 
            "Sabrina", 
            "Tom and Huck", 
            "Sudden Death", 
            "GoldenEye"
            ]
        }
    return respuesta


@router.get("/votos_titulo/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion: str) -> dict:
    """Retorna el titulo, el año, la cantidad de votos 
    y el promedio de los votos de una pelicula. Retorna 
    si la cantidad de votos es igual o mayor a 2000.
    
    Args:
        titulo (str): es un titulo de una filmacion.
        
    Returns:
        dict: es un texto con los resultados.
    """
    (titulo, 
     año, 
     cantidad, 
     promedio) = calcular_votos(titulo_de_la_filmacion)
    
    if cantidad >= 2000:
        respuesta = {
            "Respuesta": (
                f'La película {titulo} '
                f'fue estrenada en el año {año}. '
                f'Tiene un total de {cantidad} votos '
                f'y su promedio es {promedio}.'
                )
        }
    else:
        respuesta = {
            "Respuesta": (
                f'No se retorna valores '
                f'porque la película {titulo} '
                f'tiene menos de 2000 votos.'
                )
        }
    return respuesta