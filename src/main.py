from fastapi import FastAPI
import src.scripts.querymovies as query


app = FastAPI()


@app.get("/")
async def root():
    info_del_proyecto = {
        "Proyecto": "Proyecto individual MVP de un sistema de recomendación de películas",
        "Autor": "Francisco Hugo Lezik",
        "Curso": "Curso de Ciencia de Datos de Henry, cohorte 10"
    }
    mapa_de_sitio = {
        "/": "Pagina principal",
        "/cantidad_mes/mes_en_español": "Devuelve la cantidad de peliculas estrenadas en un determinado mes escrito en español.",
        "/cantidad_dia/dia_en_español": "Devuelve la cantidad de peliculas estrenadas en un determinado dia escrito en español.",
        "/score_titulo/titulo_de_la_filmacion": "Devuelve el año en que fue estrenada una pelicula y su popularidad.",
        "/votos_titulo/titulo_de_la_filmacion": "Devuelve el año en que fue estrenada una pelicula, la cantidad de votos y el promedio de votos.",
        "/actor/nombre_del_actor": "Devuelve la cantidad de peliculas en las que participo un actor, la cantidad de peliculas con datos de retorno, el retorno total y el retorno promedio",
        "/director/nombre_del_director": "Devuelve la cantidad de peliculas que dirigio un director, la cantidad de peliculas con datos de retorno y el retorno total. Ademas devuelve cada pelicula con su fecha de estreno, su retorno individual, costo y ganancia."
    }
    precondicion = {
        "Nombres": "Los nombres deben estar escritos respetando las mayusculas y minusculas como estan en el dataset."
    }
    return (info_del_proyecto, mapa_de_sitio, precondicion)


@app.get("/cantidad_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    """
        Proposito: devuelve la cantidad de películas que fueron estrenadas en el mes dado como argumento.
        Precondicion: el mes dado como argumento debe estar en español sino da error.
    """
    cantidad = query.cantidad_filmaciones_mes(mes)
    respuesta = {
        "Cantidad de peliculas": cantidad, 
        "Fueron estrenadas en el mes de": mes
    }
    return(respuesta)


@app.get("/cantidad_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str):
    """
        Proposito: devuelve la cantidad de películas que fueron estrenadas en el dia dado como argumento.
        Precondicion: el dia dado como argumento debe estar en español sino da error.
    """
    cantidad = query.cantidad_filmaciones_dia(dia)
    respuesta = {
        "Cantidad de peliculas": cantidad, 
        "Fueron estrenadas en los días": dia
    }
    return(respuesta)


@app.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str):
    """
        Proposito: devuelve el año y la popularidad de la pelicula dada como argumento.
        Precondicion: el titulo de la pelicula debe estar en el dataset y estar 
        escrito respetando las minusculas y mayusculas del titulo sino da error. 
        Si se conoce el nombre de una pelicula hecha en un pais no hispano se debe 
        introducir su nombre en el idioma original.
    """
    año, score = query.score_titulo(titulo_de_la_filmacion)
    respuesta = {
        "La película": titulo_de_la_filmacion, 
        "Fue estrenada en el año": año, 
        "Tiene un score/popularidad de": score
    }
    return(respuesta)


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
    año, cantidad_de_votos, promedio_de_votos = query.votos_titulo(titulo_de_la_filmacion)
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
    promedio) = query.get_actor(nombre_actor)
    respuesta = {
        "El actor": nombre_actor, 
        "Ha participado en": f"{total_peliculas} peliculas", 
        "Solo hay datos de retorno de": f"{peliculas_con_datos} peliculas",
        "El actor logró un retorno total de las peliculas, cuyo retorno figura en el dataset, de": total, 
        "Tiene un promedio de": f"{promedio} por película cuyo retorno figura en el dataset."
    }
    return(respuesta)


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
     peliculas) = query.get_director(nombre_director)
    director = {
        "Director": nombre_director, 
        "Cantidad de peliculas dirigidas": cantidad,
        "Cantidad de peliculas dirigidas con datos de retorno registrados en el dataset": cantidad_con_retorno,
        "Exito total a traves del retorno": total_retorno
    }
    return(director, {f"Peliculas dirigidas por {nombre_director} con retorno registrado en el dataset": peliculas})