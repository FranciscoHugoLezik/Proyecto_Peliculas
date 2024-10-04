import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.scripts import movies_query as m
from src.scripts import credits_query as c


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    informacion = {
        "Proyecto": """Proyecto individual MVP de un sistema de 
                       recomendación de películas""",
        "Autor": "Francisco Hugo Lezik",
        "Curso": "Curso de Ciencia de Datos de Henry, cohorte 10"
    }
    
    mapa_del_sitio = {
        "/": "Pagina principal",
        "/cantidad_mes/mes_en_español": """Devuelve la cantidad de peliculas 
                                           estrenadas en un determinado mes 
                                           escrito en español.""",
        "/cantidad_dia/dia_en_español": """Devuelve la cantidad de peliculas 
                                           estrenadas en un determinado dia 
                                           escrito en español.""",
        "/score_titulo/titulo_de_la_filmacion": """Devuelve el año en que fue 
                                                   estrenada una pelicula y su 
                                                   popularidad.""",
        "/votos_titulo/titulo_de_la_filmacion": """Devuelve el año en que fue 
                                                   estrenada una pelicula, la 
                                                   cantidad de votos y el 
                                                   promedio de votos.""",
        "/actor/nombre_del_actor": """Devuelve la cantidad de peliculas en las 
                                      que participo un actor, la cantidad que 
                                      tiene retorno, el retorno total y el 
                                      retorno promedio""",
        "/director/nombre_del_director": """Devuelve la cantidad de peliculas 
                                            que dirigio un director, la cantidad 
                                            que tiene retorno, el retorno total 
                                            y cada pelicula con su fecha de 
                                            estreno, su retorno individual, 
                                            costo y ganancia."""
    }
        
    precondicion = {
        "Precondicion": """Los titulos y nombres deben estar escritos, respetando 
                           las mayusculas y minusculas, como estan en el dataset."""
    }

    html_content = "<html><body>"
    for key, value in informacion.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
        
    for key, value in mapa_del_sitio.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
        
    html_content += f"<p><strong>Precondicion:</strong> {precondicion['Precondicion']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/cantidad_mes", response_class=HTMLResponse)
async def default_cantidad_filmaciones_mes():
    """
    Propósito: devuelve un mensaje predeterminado cuando no se proporciona un mes.
    """
    explicacion = {
        "Mensaje": """Tenes que proporcionar en la URL un mes, en español, 
                      por ejemplo: /cantidad_mes/marzo"""
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Mensaje:</strong> {explicacion['Mensaje']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/cantidad_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    """
        Proposito: devuelve la cantidad de películas que fueron estrenadas en el mes dado como argumento.
        Precondicion: el mes dado como argumento debe estar en español sino da error.
    """
    cantidad = m.cantidad_filmaciones_mes(mes)
    respuesta = {
        "Cantidad de peliculas": cantidad, 
        "Fueron estrenadas en el mes de": mes
    }
    return(respuesta)


@app.get("/cantidad_dia", response_class=HTMLResponse)
async def default_cantidad_filmaciones_dia():
    """
    Propósito: devuelve un mensaje predeterminado cuando no se proporciona un dia.
    """
    explicacion = {
        "Mensaje": """Tenes que proporcionar en la URL un dia, en español, 
                      por ejemplo: /cantidad_dia/lunes"""
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Mensaje:</strong> {explicacion['Mensaje']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/cantidad_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str):
    """
        Proposito: devuelve la cantidad de películas que fueron estrenadas en el dia dado como argumento.
        Precondicion: el dia dado como argumento debe estar en español sino da error.
    """
    cantidad = m.cantidad_filmaciones_dia(dia)
    respuesta = {
        "Cantidad de peliculas": cantidad, 
        "Fueron estrenadas en los días": dia
    }
    return(respuesta)


@app.get("/score_titulo", response_class=HTMLResponse)
async def default_score_titulo():
    """
    Propósito: devuelve un mensaje predeterminado cuando no se proporciona un titulo.
    """
    explicacion = {
        "Mensaje": """Tenes que proporcionar en la URL el titulo, en ingles, 
                      de una pelicula. Por ejemplo: /score_titulo/lunes"""
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Mensaje:</strong> {explicacion['Mensaje']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str):
    """
        Proposito: devuelve el año y la popularidad de la pelicula dada como argumento.
        Precondicion: el titulo de la pelicula debe estar en el dataset y estar 
        escrito respetando las minusculas y mayusculas del titulo sino da error. 
        Si se conoce el nombre de una pelicula hecha en un pais no hispano se debe 
        introducir su nombre en el idioma original.
    """
    año, score = m.score_titulo(titulo_de_la_filmacion)
    respuesta = {
        "La película": titulo_de_la_filmacion, 
        "Fue estrenada en el año": año, 
        "Tiene un score/popularidad de": score
    }
    return(respuesta)


@app.get("/votos_titulo", response_class=HTMLResponse)
async def default_votos_titulo():
    """
    Propósito: devuelve un mensaje predeterminado cuando no se proporciona un titulo.
    """
    explicacion = {
        "Mensaje": """Tenes que proporcionar en la URL el titulo, en ingles, 
                      de una pelicula. Por ejemplo: /votos_titulo/lunes"""
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Mensaje:</strong> {explicacion['Mensaje']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/votos_titulo/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion: str):
    """
        Proposito: devuelve el año, la cantidad de votos y el promedio de los votos
        de la pelicula dada como argumento. Si la cantidad de votos es menor a 2000 
        no devuelve ningun valor.
        Precondicion: el titulo de la pelicula debe estar en el dataset y estar 
        escrito respetando las minusculas y mayusculas del titulo sino da error.
        Si se conoce el nombre de una pelicula hecha en un pais no hispano se debe 
        introducir su nombre en el idioma original.
    """
    año, cantidad_de_votos, promedio_de_votos = m.votos_titulo(titulo_de_la_filmacion)
    if cantidad_de_votos >= 2000:
        respuesta = {
            "La película": titulo_de_la_filmacion, 
            "Fue estrenada en el año": año, 
            "Cuenta con un total de votos de": cantidad_de_votos, 
            "Con un promedio de": promedio_de_votos
        }
    else:
        respuesta = {
            "La película": f"{titulo_de_la_filmacion} tiene que tener 2000 o mas votos para devolver los valores solicitados."
        }
    return(respuesta)


@app.get("/actor", response_class=HTMLResponse)
async def default_get_actor():
    """
    Propósito: devuelve un mensaje predeterminado cuando no se proporciona el nombre de un actor.
    """
    explicacion = {
        "Mensaje": """Tenes que proporcionar en la URL el nombre de un actor. 
                      Por ejemplo: /actor/Tom Hanks"""
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Mensaje:</strong> {explicacion['Mensaje']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/actor/{nombre_actor}")
async def get_actor(nombre_actor: str):
    """
        Proposito: devuelve el total de peliculas en las que participo el actor, 
        el total de peliculas que tienen dato de retorno, el total de retorno y el 
        promedio de retorno por pelicula.
        Precondicion: el nombre del actor debe estar en el dataset y estar 
        escrito respetando las minusculas y mayusculas del nombre sino da error.
    """
    (total_peliculas, 
    peliculas_con_datos, 
    total,
    promedio) = c.get_actor(nombre_actor)
    respuesta = {
        "El actor": nombre_actor, 
        "Ha participado en": f"{total_peliculas} peliculas", 
        "Solo hay datos de retorno de": f"{peliculas_con_datos} peliculas",
        "El actor logró un retorno total de las peliculas, cuyo retorno figura en el dataset, de": total, 
        "Tiene un promedio de": f"{promedio} por película cuyo retorno figura en el dataset."
    }
    return(respuesta)


@app.get("/director", response_class=HTMLResponse)
async def default_get_director():
    """
    Propósito: devuelve un mensaje predeterminado cuando no se proporciona el nombre de un director.
    """
    explicacion = {
        "Mensaje": """Tenes que proporcionar en la URL el nombre de un director. 
                      Por ejemplo: /director/John Lasseter"""
    }
    html_content = "<html><body>"
    html_content += f"<p><strong>Mensaje:</strong> {explicacion['Mensaje']}</p>"
    html_content += "</body></html>"
    return (HTMLResponse(content=html_content))


@app.get("/director/{nombre_director}")
async def get_director(nombre_director: str):
    """
        Proposito: devuelve el total de peliculas que dirigio el director, 
        el total de peliculas que tienen dato de retorno y el total de retorno. 
        Ademas devuelve el nombre de cada pelicula con la fecha de lanzamiento, 
        el retorno individual, el costo y la ganancia.
        Precondicion: el nombre del director debe estar en el dataset y estar 
        escrito respetando las minusculas y mayusculas del nombre sino da error.
    """
    (cantidad, 
     cantidad_con_retorno, 
     total_retorno, 
     peliculas) = c.get_director(nombre_director)
    director = {
        "Director": nombre_director, 
        "Cantidad de peliculas dirigidas": cantidad,
        "Cantidad de peliculas dirigidas con datos de retorno registrados en el dataset": cantidad_con_retorno,
        "Exito total a traves del retorno": total_retorno
    }
    return(director, {f"Peliculas dirigidas por {nombre_director} con retorno registrado en el dataset": peliculas})