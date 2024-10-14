from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.modules.credits import credits as c


router = APIRouter()


@router.get("/actor", 
            response_class=HTMLResponse)
async def default_get_actor() -> HTMLResponse:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona el titulo de una filmacion 
    en la URL.
    
    Returns:
        HTMLResponse: es un texto con la explicacion 
        del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": """Retorna el nombre del actor, el total 
                     de peliculas en las que participo, la 
                     cantidad que tiene datos de retorno, el 
                     total de retorno y su promedio.""", 
        "Uso": """Tenes que agregarle a esta URL el 
               nombre de un actor. La primera letra de cada 
               nombre y apellido debe estar en mayúscula y el 
               resto en minúscula. Por ejemplo: 
               /actor/Tom Hanks""", 
        "Algunos actores disponibles": (
            "Tom Hanks", 
            "Tim Allen", 
            "Don Rickles", 
            "Jim Varney", 
            "Wallace Shawn", 
            "John Ratzenberger", 
            "Annie Potts", 
            "John Morris", 
            "Erik von Detten", 
            "Laurie Metcalf"
        )
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@router.get("/actor/{nombre}", 
            response_class=HTMLResponse)
async def get_actor(nombre: str) -> HTMLResponse:
    """Obtiene el nombre del actor, la cantidad de 
    peliculas en las que participo, la cantidad 
    que tiene datos de retorno, el total de 
    retorno y su promedio.
    
    Args:
        nombre (str): es el nombre de un actor.
        
    Returns:
        HTMLResponse: es un texto con los resultados.
    """
    (total_peliculas, 
    total_con_retorno, 
    total_retorno,
    promedio_retorno) = c.get_actor(nombre)
    
    total_peliculas = str(total_peliculas)
    total_con_retorno = str(total_con_retorno)
    total_retorno = str(total_retorno)
    promedio_retorno = str(promedio_retorno)
    
    respuesta = (
        "El actor", 
        nombre, 
        "ha participado en", 
        total_peliculas, 
        "peliculas.", 
        "Hay", 
        total_con_retorno, 
        "peliculas con datos de retorno. "
        "El actor logró un retorno total de", 
        total_retorno, 
        "y su promedio es de", 
        promedio_retorno, 
        "por pelicula."
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