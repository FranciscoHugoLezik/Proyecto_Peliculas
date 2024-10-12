from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.modules.credits import credits as c


router = APIRouter()


@router.get("/director", 
            response_class=HTMLResponse)
async def default_get_director() -> HTMLResponse:
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
               nombre de un director. Por ejemplo: 
               /director/John Lasseter"""
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@router.get("/director/{nombre}", 
            response_class=HTMLResponse)
async def get_director(nombre: str) -> HTMLResponse:
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
    (total_peliculas, 
     total_con_retorno, 
     total_retorno, 
     peliculas) = c.get_director(nombre)
    total_peliculas = str(total_peliculas)
    total_con_retorno = str(total_con_retorno)
    total_retorno = str(total_retorno)
    director = (
        "El director", 
        nombre, 
        "ha dirigido", 
        total_peliculas, 
        "peliculas.",
        "Hay", 
        total_con_retorno, 
        "peliculas con retorno registrado.", 
        "El retorno total es", 
        total_retorno,
        "."
    )
    director = ' '.join(director)
    respuesta = {
        "Director": director, 
        "Introduccion": """Las peliculas, con retorno 
                        registrado, son las siguientes:""", 
        "Peliculas": peliculas
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Respuesta:</strong></p>"
    html_content += "<br><br>"
    html_content += f"<p>{respuesta['Director']}</p>"
    html_content += "<br><br>"
    html_content += f"<p>{respuesta['Introduccion']}</p>"
    html_content += "<br><br>"
    for pelicula in peliculas:
        for key, value in pelicula.items():
            html_content += f"<p><strong>{key}:</strong> {value}</p>"
        html_content += "<br><br>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))