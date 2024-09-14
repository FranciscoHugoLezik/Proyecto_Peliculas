from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>FastAPI App</title>
        </head>
        <body>
            <h1>Servicio de agregación de plataformas de streaming</h1>
            <ul>
                <li><a href="/cantidad_mes">Cantidad de películas por mes</a></li>
                <li><a href="/cantidad_dia">Cantidad de películas por día</a></li>
                <li><a href="/score_titulo">Score de una película</a></li>
                <li><a href="/votos_titulo">Votos de una pelicula</a></li>
                <li><a href="/actor">Información de un actor</a></li>
                <li><a href="/director">Información de un director</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/cantidad_mes")
async def cantidad_filmaciones_mes():
    answer = {
        "quantity": 10, 
        "words": "peliculas fueron extrenadas en el mes de", 
        "month": "Octubre"
    }
    return(answer)


@app.get("/cantidad_dia")
async def cantidad_filmaciones_dia():
    answer = {
        "quantity": 2, 
        "words": "peliculas fueron estrenadas en los días", 
        "day": "martes"
    }
    return(answer)


@app.get("/score_titulo")
async def score_titulo():
    answer = {
        "words_1": "La película", 
        "movie": "Star Wars, La Venganza de los Sith,", 
        "words_2": "fue estrenada en el año", 
        "year": 2005, 
        "words_3": "con un score/popularidad de", 
        "score": 85.5
    }
    return(answer)


@app.get("/votos_titulo")
async def votos_titulo():
    answer = {
        "words_1": "La película", 
        "movie": "Star Wars, La Venganza de los Sith,", 
        "words_2": "fue estrenada en el año", 
        "year": 2005, 
        "words_3": ". La misma cuenta con un total de", 
        "vote_count": 1000, 
        "words_4": "valoraciones, con un promedio de", 
        "vote_average": 9.3
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