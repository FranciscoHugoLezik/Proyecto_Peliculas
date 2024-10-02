import pandas as pd

if __name__ == "__main__":
    import auxiliary as aux
else:
    from src.scripts import auxiliary as aux


def cantidad_filmaciones_mes(mes):
    meses = aux.get_meses()
    cantidades = meses.value_counts()
    numero_mes = aux.get_numero_mes(mes)
    cantidad = int(cantidades[numero_mes])
    return (cantidad)


def cantidad_filmaciones_dia(dia):
    dias = aux.get_dias()
    cantidades = dias.value_counts()
    dia_en_ingles = aux.get_dia_en_ingles(dia)
    cantidad = int(cantidades[dia_en_ingles])
    return (cantidad)


def score_titulo(titulo):
    filmacion = aux.get_filmacion(titulo)
    año = int(filmacion['release_year'])
    popularidad = float(filmacion['popularity'])
    return (año, 
            popularidad)


def votos_titulo(titulo): 
    filmacion = aux.get_filmacion(titulo)
    año = int(filmacion['release_year'])
    cantidad = int(filmacion['vote_count'])
    promedio = float(filmacion['vote_average'])
    return (año, 
            cantidad, 
            promedio)


def get_actor(nombre):
    sus_peliculas = aux.get_movies_id(nombre, 
                                      'cast')
    cantidad = len(sus_peliculas)
    detalles = aux.get_peliculas('id', 
                                 'return')
    peliculas = pd.merge(sus_peliculas, 
                         detalles, 
                         on='movie_id')
    con_retorno = aux.filtrar_por_retorno(peliculas)
    cantidad_con_retorno = len(con_retorno)
    total = con_retorno['return'].sum().round(2)
    promedio = con_retorno['return'].mean().round(2)
    return(cantidad, 
           cantidad_con_retorno, 
           total, 
           promedio)


def get_director(nombre):
    sus_peliculas = aux.get_movies_id(nombre, 
                                      'crew')
    sus_peliculas = sus_peliculas.query('job == "Director"')
    cantidad = len(sus_peliculas)
    detalles = aux.get_peliculas('id', 
                                 'title', 
                                 'release_date', 
                                 'return', 
                                 'budget', 
                                 'revenue')
    peliculas = pd.merge(sus_peliculas, 
                         detalles, 
                         on='movie_id')
    con_retorno = aux.filtrar_por_retorno(peliculas)
    cantidad_con_retorno = len(con_retorno)
    total = con_retorno['return'].sum().round(2)
    peliculas = aux.procesar_peliculas(peliculas)
    return (cantidad, 
            cantidad_con_retorno, 
            total, 
            peliculas)