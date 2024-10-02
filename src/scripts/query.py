import pandas as pd

if __name__ == "__main__":
    import constant as c
    import auxiliary as aux
else:
    from src.scripts import constant as c
    from src.scripts import auxiliary as aux


def cantidad_filmaciones_mes(mes):
    solo_meses = c.MOVIES['release_date'].dt.month
    cantidad_por_mes = solo_meses.value_counts()
    
    mes = int(c.MESES.get(mes))
    
    cantidad = int(cantidad_por_mes[mes])
    
    return (cantidad)


def cantidad_filmaciones_dia(dia):
    solo_dias = c.MOVIES['release_date'].dt.strftime('%A')
    cantidad_por_dia = solo_dias.value_counts()
    
    dia = c.DIAS.get(dia)
    
    cantidad = int(cantidad_por_dia[dia])
    
    return (cantidad)


def score_titulo(titulo):
    movies = c.MOVIES.copy()
    movies.set_index('title', 
                     inplace=True)
    filmación = movies.loc[titulo]
    
    año = int(filmación['release_year'])
    popularidad = float(filmación['popularity'])
    
    return (año, 
            popularidad)


def votos_titulo(titulo): 
    movies = c.MOVIES.copy()
    movies.set_index('title', 
                     inplace=True)
    filmación = movies.loc[titulo]
    
    año = int(filmación['release_year'])
    cantidad = int(filmación['vote_count'])
    promedio = float(filmación['vote_average'])
    
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