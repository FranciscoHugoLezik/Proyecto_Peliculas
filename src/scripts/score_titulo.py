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
               de una pelicula. Por ejemplo: 
               /score_titulo/Toy Story"""
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