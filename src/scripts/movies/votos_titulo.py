from fastapi import APIRouter

from src.modules.movies.functions.votos_titulo \
    import votos_titulo as calcular_votos


router = APIRouter()


@router.get("/votos_titulo/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion: str) -> dict:
    """Retorna el titulo, el año, la cantidad de votos 
    y el promedio de los votos de una pelicula. Retorna 
    si la cantidad de votos es igual o mayor a 2000.
    
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