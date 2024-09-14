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
                <li><a href="/cantidad_mes">Cantidad de Filmaciones por Mes</a></li>
                <li><a href="/otra_funcion">Otra Función</a></li>
                <!-- Agrega más enlaces aquí -->
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/cantidad_mes")
async def cantidad_filmaciones_mes():
    answer = {
        "cantidad": 10, 
        "sentence": "peliculas fueron extrenadas en el mes de", 
        "mes": "Octubre"
    }
    print(answer)
    return(answer)


@app.get("/otra_funcion")
async def otra_funcion():
    return {"message": "Esta es otra función"}


"""
@app.get("/cantidad_dia")
async def cantidad_filmaciones_dia():
    answer = (2, 'peliculas fueron estrenadas en los días', 'martes')
    print(answer)
    return(answer)


@app.get("/score_titulo")
async def score_titulo():
    answer = ('La película', 'Star Wars, La Venganza de los Sith', 'fue estrenada en el año', \
             2005, 'con un score/popularidad de', 85.5)
    print(answer)
    return(answer)

@app.get("/votos_titulo")
async def votos_titulo():
    answer = ('La película', 'Star Wars, La Venganza de los Sith', 
             'fue estrenada en el año', 2005, '.', 'La misma cuenta con un total de', 
             1000, 'valoraciones, con un promedio de', 9.3)
    print(answer)
    return(answer)


@app.get("/actor")
async def get_actor():
    answer = ('El actor', 'Pedro', 'ha participado en', 20, 
             'películas. Logró un retorno de', 20000000, 
             'de dolares con un promedio de', 1000000, 'de dolares por película.')
    print(answer)
    return(answer)

@app.get("/director")
async def get_director():
    answer = ('El director', 'Juan', 'que ha obtenido un exito que medido en dolares es de', 
             12000000, 'de dolares. Las películas que dirigio son:','\n',
             'La Pelicula', 'estrenada en el año', 2000, 'con un retorno de', 
             40000000, 'un costo de', 1000000, 'y una ganancia de', 30000000,'.','\n',
             'La Pelicula 2', 'estrenada en el año', 2003, 'con un retorno de', 
             70000000, 'un costo de', 2000000, 'y una ganancia de', 40000000,'.','\n',
             'La Pelicula 3', 'estrenada en el año', 2007, 'con un retorno de', 
             80000000, 'un costo de', 3000000, 'y una ganancia de', 50000000,'.')
    print(answer)
    return(answer)
"""