from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def cantidad_filmaciones_mes():
    return 10, 'peliculas fueron extrenadas en el mes de', 'Octubre'


@app.get("/")
async def cantidad_filmaciones_dia():
    return 2, 'peliculas fueron estrenadas en los días', 'martes'


@app.get("/")
async def score_titulo():
    return 'La película', 'Star Wars, La Venganza de los Sith', 'fue estrenada en el año', \
        2005, 'con un score/popularidad de', 85.5


@app.get("/")
async def votos_titulo():
    return ('La película', 'Star Wars, La Venganza de los Sith', 
            'fue estrenada en el año', 2005, '.', 'La misma cuenta con un total de', 
            1000, 'valoraciones, con un promedio de', 9.3)


@app.get("/")
async def get_actor():
    return ('El actor', 'Pedro', 'ha participado en', 20, 
            'películas. Logró un retorno de', 20000000, 
            'de dolares con un promedio de', 1000000, 'de dolares por película.')


@app.get("/")
async def get_director():
    return ('El director', 'Juan', 'que ha obtenido un exito que medido en dolares es de', 
            12000000, 'de dolares. Las películas que dirigio son:','\n',
            'La Pelicula', 'estrenada en el año', 2000, 'con un retorno de', 
            40000000, 'un costo de', 1000000, 'y una ganancia de', 30000000,'.','\n',
            'La Pelicula 2', 'estrenada en el año', 2003, 'con un retorno de', 
            70000000, 'un costo de', 2000000, 'y una ganancia de', 40000000,'.','\n',
            'La Pelicula 3', 'estrenada en el año', 2007, 'con un retorno de', 
            80000000, 'un costo de', 3000000, 'y una ganancia de', 50000000,'.')