from fastapi import APIRouter

from src.modules.movies.functions.score_titulo \
    import score_titulo as calcular_score


router = APIRouter()


@router.get("/score_titulo")
async def default_score_titulo() -> dict:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona el titulo de una filmacion 
    en la URL.
    
    Returns:
        dict: es un texto con la explicacion 
        del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": (
            "Retorna el titulo, el año y "
            "la popularidad de una pelicula."
            ), 
        "Uso": (
            "Tenes que agregarle a esta URL "
            "el titulo de una pelicula. "
            "Por ejemplo: /score_titulo/Toy Story"
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


@router.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str) -> dict:
    """Retorna el titulo, el año y la popularidad de 
    una pelicula.
    
    Args: 
        titulo (str): es un titulo de una filmacion.
        
    Returns:
        dict: Es un texto con los resultados.
    """
    (titulo, 
     año, 
     score) = calcular_score(titulo_de_la_filmacion)
    
    respuesta = {
        "Respuesta": (
            f'La película {titulo} '
            f'fue estrenada en el año {año} '
            f'y tiene un score de {score}'
            )
    }
    return respuesta