from fastapi import FastAPI
import src.scripts.query_movies as query


app = FastAPI()


@app.get("/cantidad_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    cantidad = query.cantidad_filmaciones_mes(mes)
    answer = {
        "quantity": cantidad, 
        "words": "peliculas fueron estrenadas en el mes de", 
        "month": mes
    }
    return(answer)


@app.get("/cantidad_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str):
    cantidad = query.cantidad_filmaciones_dia(dia)
    answer = {
        "quantity": cantidad, 
        "words": "peliculas fueron estrenadas en los días", 
        "day": dia
    }
    return(answer)


@app.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str):
    año, score = query.score_titulo(titulo_de_la_filmacion)
    answer = {
        "words_1": "La película", 
        "movie": titulo_de_la_filmacion, 
        "words_2": "fue estrenada en el año", 
        "year": año, 
        "words_3": "con un score/popularidad de", 
        "score": score
    }
    return(answer)


@app.get("/votos_titulo/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion: str):
    año, cantidad_de_votos, promedio_de_votos = query.votos_titulo(titulo_de_la_filmacion)
    if cantidad_de_votos >= 2000:
        answer = {
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
        answer = {
            "words_1": "La película tiene que tener 2000 o mas votos para devolver los valores solicitados.",
            "words_2": "La película",
            "movie": titulo_de_la_filmacion,
            "words_3": "no cumple con la cantidad minima de votos para devolver valores."
        }
    return(answer)


@app.get("/actor")
async def get_actor():
    answer = {
        "words_1": "El actor", 
        "actor": "Pedro", 
        "words_2": "ha participado en", 
        "movies_number": 20, 
        "words_3": "películas.", 
        "words_4": "Logró un retorno de", 
        "return": 20000000, 
        "words_5": "de dolares con un promedio de", 
        "mean": 1000000, 
        "words_6": "de dolares por película."
    }
    return(answer)


@app.get("/director")
async def get_director():
    director = {
        "words_1": "El director", 
        "director": "Juan", 
        "words_2": "con todas sus peliculas a tenido un retorno de", 
        "total_revenue": 190000000, 
        "words_3": "de dolares.",
        "words_4": "Las películas que dirigio son:", 
        "movies": {
            "movie_1": {
                "title": "La Pelicula", 
                "words_1": "estrenada en el año", 
                "year": 2000,
                "words_2": "con un retorno de", 
                "revenue": 40000000, 
                "words_3": "tuvo un costo de", 
                "budget": 1000000, 
                "words_4": "y una ganancia de", 
                "benefit": 30000000, 
                "words_5": "."
            }, 
            "movie_2": {
                "title": "La Pelicula 2", 
                "words_1": "estrenada en el año", 
                "year": 2003,
                "words_2": "con un retorno de", 
                "revenue": 70000000, 
                "words_3": "tuvo un costo de", 
                "budget": 2000000, 
                "words_4": "y una ganancia de", 
                "benefit": 40000000, 
                "words_5": "."
            },
            "movie_3": {
                "title": "La Pelicula 3", 
                "words_1": "estrenada en el año", 
                "year": 2007,
                "words_2": "con un retorno de", 
                "revenue": 80000000, 
                "words_3": "tuvo un costo de", 
                "budget": 3000000, 
                "words_4": "y una ganancia de", 
                "benefit": 50000000, 
                "words_5": "."
            }
        }
    }
    return(director)