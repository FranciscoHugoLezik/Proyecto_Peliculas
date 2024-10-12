from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.modules.movies import movies as m


router = APIRouter()


@router.get("/cantidad_mes", 
            response_class=HTMLResponse)
async def default_cantidad_filmaciones_mes() -> HTMLResponse:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona un mes, en español, en la URL.
    
    Returns:
        respuesta (HTMLResponse): Es un texto con la 
        explicacion del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": """Retorna la cantidad de peliculas 
                     que fueron estrenadas en un mes 
                     escrito en español.""",
        "Uso": """Tenes que agregarle a esta URL un mes 
               en español. Por ejemplo: /cantidad_mes/enero"""
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"
    
    return (HTMLResponse(content=html_content))


@router.get("/cantidad_mes/{mes}", 
         response_class=HTMLResponse)
async def cantidad_filmaciones_mes(mes: str) -> HTMLResponse:
    """Retorna la cantidad de filmaciones que 
    fueron estrenadas en el mes dado como argumento.
    
    Args: 
        mes (str): es un mes en español.
        
    Returns:
        respuesta (HTMLResponse): Es un texto con la 
        cantidad de filmaciones estrenadas en un mes 
        en particular.
    """
    cantidad = m.cantidad_filmaciones_mes(mes)
    cantidad = str(cantidad)
    respuesta = ("Fueron estrenadas", 
                 cantidad, 
                 "peliculas en el mes de", 
                 mes)
    respuesta = ' '.join(respuesta)
    respuesta = {
        "Respuesta": respuesta
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Respuesta:</strong> \n"
    html_content += f"{respuesta['Respuesta']}</p>"
    html_content += "</body></html>"

    return (HTMLResponse(content=html_content))