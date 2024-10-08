if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.scripts import movies_query as m
from src.scripts import credits_query as c


app = FastAPI()


@app.get("/", 
         response_class=HTMLResponse)
async def root():
    datos_del_autor = {
        "Autor": "Francisco Hugo Lezik",
        "Curso": "Curso de Ciencia de Datos de Henry, cohorte 10"
    }
    mapa_del_sitio = {
        "/": "Pagina principal",
        "/cantidad_mes/mes": """Retorna la cantidad de peliculas 
                             estrenadas en un determinado mes 
                             escrito en español.""",
        "/cantidad_dia/dia": """Retorna la cantidad de peliculas 
                             estrenadas en un determinado dia 
                             escrito en español.""",
        "/score_titulo/titulo": """Retorna el titulo de la pelicula, 
                                el año en que fue estrenada y su 
                                popularidad.""",
        "/votos_titulo/titulo": """Retorna el titulo de la pelicula, 
                                el año en que fue estrenada, la 
                                cantidad de votos y el promedio 
                                de votos.""",
        "/actor/nombre": """Retorna el nombre del actor, la cantidad de 
                         peliculas en las que participo, la cantidad 
                         que tiene retorno, el retorno total y el 
                         retorno promedio.""",
        "/director/nombre": """Retorna el nombre del director, la 
                            cantidad de peliculas que dirigio, la 
                            cantidad que tiene retorno y el retorno 
                            total. Ademas retorna el nombre de cada 
                            pelicula, su fecha de estreno, su retorno 
                            individual, su costo y su ganancia."""
    } 
    precondicion = {
        "Precondicion": """Los titulos y nombres deben estar escritos, respetando 
                        las mayusculas y minusculas, como estan en el dataset."""
    }

    html_content = "<html><body>"
    html_content += "<p><strong>Proyecto Individual MVP de un Sistema \n"
    html_content += "de Recomendación de Peliculas</strong></p>"
    html_content += "<br><br>"
    
    for key, value in datos_del_autor.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "<br><br>"
    
    html_content += "<p><strong>Mapa del sitio:</strong></p>"
    for key, value in mapa_del_sitio.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "<br><br>"        

    html_content += f"<p><strong>Precondicion:</strong> \n"
    html_content += f"{precondicion['Precondicion']}</p>"
    html_content += "</body></html>"
    
    return (HTMLResponse(content=html_content))


@app.get("/cantidad_mes", 
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


@app.get("/cantidad_mes/{mes}", 
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


@app.get("/cantidad_dia", 
         response_class=HTMLResponse)
async def default_cantidad_filmaciones_dia() -> HTMLResponse:
    """Retorna una explicacion de la funcion y de su uso 
    cuando no se proporciona un dia, en español, en la URL.
    
    Returns:
        respuesta (HTMLResponse): Es un texto con la 
        explicacion del proposito de la funcion y de su uso.
    """
    respuesta = {
        "Proposito": """Retorna la cantidad de peliculas 
                     que fueron estrenadas en un dia 
                     escrito en español.""",
        "Uso": """Tenes que agregarle a esta URL un dia 
               en español. Por ejemplo: /cantidad_dia/lunes"""
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/cantidad_dia/{dia}", 
         response_class=HTMLResponse)
async def cantidad_filmaciones_dia(dia: str) -> HTMLResponse:
    """Retorna la cantidad de filmaciones que 
    fueron estrenadas en el dia dado como argumento.
    
    Args: 
        dia (str): es un dia en español.
        
    Returns:
        respuesta (HTMLResponse): Es un texto con la 
        cantidad de filmaciones estrenadas en un dia 
        en particular.
    """
    cantidad = m.cantidad_filmaciones_dia(dia)
    cantidad = str(cantidad)
    respuesta = ("Fueron estrenadas", 
                 cantidad, 
                 "peliculas en el dia", 
                 dia)
    respuesta = ' '.join(respuesta)
    respuesta = {
        "Respuesta": respuesta
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Respuesta:</strong> \n"
    html_content += f"{respuesta['Respuesta']}</p>"
    html_content += "</body></html>"

    return (HTMLResponse(content=html_content))


@app.get("/score_titulo", 
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


@app.get("/score_titulo/{titulo}", 
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


@app.get("/votos_titulo", 
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


@app.get("/votos_titulo/{titulo}", 
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


@app.get("/actor", 
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
               nombre de un actor. Por ejemplo: 
               /actor/Tom Hanks"""
    }
    html_content = "<html><body>"
    for key, value in respuesta.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/actor/{nombre}", 
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


@app.get("/director", 
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


@app.get("/director/{nombre}", 
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