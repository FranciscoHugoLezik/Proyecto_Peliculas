from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def root() -> dict:
    """Retorna los datos de la app.
    
    Return: \n
        dict: es un texto con los datos.
    """
    respuesta = {
        "Proyecto": "Sistema de Recomendación de Películas", 
        "Autor": "Francisco Hugo Lezik",
        "Academia": "Henry", 
        "Curso": "Data Science", 
        "Cohorte": "11", 
        "/": "Pagina principal",
        "/cantidad_filmaciones_mes/mes": (
            "Retorna la cantidad de peliculas " 
            "estrenadas en un determinado mes " 
            "escrito en español."
            ),
        "/cantidad_filmaciones_dia/dia": (
            "Retorna la cantidad de peliculas " 
            "estrenadas en un determinado dia " 
            "escrito en español."
            ),
        "/score_titulo/titulo_de_la_filmacion": (
            "Retorna el titulo de la pelicula, "
            "el año en que fue estrenada y su "
            "popularidad."
            ),
        "/votos_titulo/titulo_de_la_filmacion": (
            "Retorna el titulo de la pelicula, " 
            "el año en que fue estrenada, la " 
            "cantidad de votos y el promedio " 
            "de votos."
            ),
        "/get_actor/nombre_actor": (
            "Retorna el nombre del actor, la cantidad de " 
            "peliculas en las que participo, la cantidad " 
            "que tiene retorno, el retorno total y el " 
            "retorno promedio."
            ),
        "/get_director/nombre_director": (
            "Retorna el nombre del director, la " 
            "cantidad de peliculas que dirigio, la " 
            "cantidad que tiene retorno y el retorno " 
            "total. Ademas retorna el nombre de cada " 
            "pelicula, su fecha de estreno, su retorno " 
            "individual, su costo y su ganancia."
            )
        }
    return respuesta