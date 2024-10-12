from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.modules.movies import movies as m


router = APIRouter()


@router.get("/votos_titulo", 
            response_class=HTMLResponse)
async def default_votos_titulo() -> HTMLResponse:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona el titulo de una filmacion 
    en la URL.
    
    Returns:
        HTMLResponse: Es un texto con la explicacion 
        del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": """Retorna el titulo, el año, la 
                     cantidad de votos y el promedio de 
                     votos de una pelicula. Si la cantidad 
                     de votos es menor a 2000 no devuelve 
                     ningun valor.""",
        "Uso": """Tenes que agregarle a esta URL el titulo 
               de una pelicula. Por ejemplo: 
               /votos_titulo/Toy Story"""
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@router.get("/votos_titulo/{titulo}", 
            response_class=HTMLResponse)
async def votos_titulo(titulo: str) -> HTMLResponse:
    """Retorna el titulo, el año, la cantidad de votos 
    y el promedio de los votos de una pelicula. Retorna 
    si la cantidad de votos es igual o mayor a 2000.
    
    Args:
        titulo (str): es un titulo de una filmacion.
        
    Returns:
        HTMLResponse: es un texto con los resultados.
    """
    (año, 
     cantidad, 
     promedio) = m.votos_titulo(titulo)
    
    if cantidad >= 2000:
        cantidad = str(cantidad)
        promedio = str(promedio)
        respuesta = (
            "La película", 
            titulo, 
            "fue estrenada en el año", 
            año, 
            ", tiene un total de", 
            cantidad, 
            "votos y su promedio es", 
            promedio
        )
    else:
        respuesta = (
            "No se retorna valores.",
            "La película", 
            titulo, 
            "tiene menos de 2000 votos."
        )
    respuesta = ' '.join(respuesta)
    respuesta = {
        "Respuesta": respuesta
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Respuesta:</strong> \n"
    html_content += f"{respuesta['Respuesta']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))