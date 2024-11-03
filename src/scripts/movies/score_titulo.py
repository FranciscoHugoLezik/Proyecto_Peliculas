from fastapi import APIRouter

from src.modules.movies.functions.score_titulo \
    import score_titulo as calcular_score


router = APIRouter()


@router.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str) -> dict:
    """Retorna el titulo, el año y la popularidad de 
    una pelicula.
    
    Arg: \n
        titulo (str): es un titulo de una filmacion.
        
    Return: \n
        dict: es un texto con los resultados.
        
    Algunos títulos disponibles para probar: \n
        Toy Story 
        Jumanji
        Grumpier Old Men
        Waiting to Exhale
        Father of the Bride Part II
        Heat
        Sabrina
        Tom and Huck
        Sudden Death
        GoldenEye
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