from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.modules.movies import movies as m


router = APIRouter()


@router.get("/score_titulo", 
            response_class=HTMLResponse)
async def default_score_titulo() -> HTMLResponse:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona el titulo de una filmacion 
    en la URL.
    
    Returns:
        respuesta (HTMLResponse): Es un texto con la 
        explicacion del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": """Retorna el titulo, el año y la 
                     popularidad de una pelicula.""", 
        "Uso": """Tenes que agregarle a esta URL el titulo 
               de una pelicula. Las palabras importantes del 
               titulo deben tener la primer letra en mayúscula 
               y el resto en minúscula. Las palabras como 'to' 
               u 'of' siempre en minuscula salvo que sean la 
               primer palabra del título. Por ejemplo: 
               /score_titulo/Toy Story""", 
        "Algunos títulos disponibles": (
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
            )
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@router.get("/score_titulo/{titulo}", 
            response_class=HTMLResponse)
async def score_titulo(titulo: str) -> HTMLResponse:
    """Retorna el titulo, el año y la popularidad de 
    una pelicula.
    
    Args: 
        titulo (str): es un titulo de una filmacion.
        
    Returns:
        HTMLResponse: Es un texto con los resultados.
    """
    año, score = m.score_titulo(titulo)
    score = str(score)
    
    respuesta = ("La película", 
                 titulo, 
                 "fue estrenada en el año", 
                 año, 
                 "y tiene un score/popularidad de", 
                 score)
    respuesta = ' '.join(respuesta)
    respuesta = {
        "Respuesta": respuesta
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"

    return (HTMLResponse(content=html_content))