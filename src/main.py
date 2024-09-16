from fastapi import FastAPI
import src.scripts.query_movies as query


app = FastAPI()


@app.get("/")
async def root():
    respuesta = {
        "proyecto": "Proyecto individual de recomendación de películas",
        "autor": "Francisco Hugo Lezik",
        "curso": "Curso de Ciencia de Datos de Henry, cohorte 10"
    }
    return (respuesta)


@app.get("/cantidad_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    cantidad = query.cantidad_filmaciones_mes(mes)
    respuesta = {
        "quantity": cantidad, 
        "words": "peliculas fueron estrenadas en el mes de", 
        "month": mes
    }
    return(respuesta)


@app.get("/cantidad_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str):
    cantidad = query.cantidad_filmaciones_dia(dia)
    respuesta = {
        "quantity": cantidad, 
        "words": "peliculas fueron estrenadas en los días", 
        "day": dia
    }
    return(respuesta)


@app.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str):
    año, score = query.score_titulo(titulo_de_la_filmacion)
    respuesta = {
        "words_1": "La película", 
        "movie": titulo_de_la_filmacion, 
        "words_2": "fue estrenada en el año", 
        "year": año, 
        "words_3": "con un score/popularidad de", 
        "score": score
    }
    return(respuesta)


@app.get("/votos_titulo/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion: str):
    año, cantidad_de_votos, promedio_de_votos = query.votos_titulo(titulo_de_la_filmacion)
    if cantidad_de_votos >= 2000:
        respuesta = {
            "words_1": "La película", 
            "movie": titulo_de_la_filmacion, 
            "words_2": "fue estrenada en el año", 
            "year": año, 
            "words_3": ". La misma cuenta con un total de", 
            "vote_count": cantidad_de_votos, 
            "words_4": "valoraciones, con un promedio de", 
            "vote_average": promedio_de_votos
        }
    else:
        respuesta = {
            "words_1": "La película tiene que tener 2000 o mas votos para devolver los valores solicitados.",
            "words_2": "La película",
            "movie": titulo_de_la_filmacion,
            "words_3": "no cumple con la cantidad minima de votos para devolver valores."
        }
    return(respuesta)


@app.get("/actor/{nombre_actor}")
async def get_actor(nombre_actor: str):
    (total_peliculas, 
    peliculas_con_datos, 
    total,
    promedio) = query.get_actor(nombre_actor)
    respuesta = {
        "words_1": "El actor", 
        "actor": nombre_actor, 
        "words_2": "ha participado en", 
        "total_movies": total_peliculas, 
        "words_3": "películas.",
        "words_4": "Solo hay datos de retorno de",
        "movies_with_return": peliculas_con_datos,
        "words_5": "peliculas.",
        "words_6": "Por lo tanto solo se usara esta cantidad de peliculas para los calculos.",
        "words_7": "El actor logró un retorno de", 
        "total": total, 
        "words_8": "con un promedio de", 
        "mean": promedio, 
        "words_9": "por película."
    }
    return(respuesta)


@app.get("/director/{nombre_director}")
async def get_director(nombre_director: str):
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