import pandas as pd

if __name__ == "__main__":
    import credits_query_auxiliary as q
else:
    from src.scripts import credits_query_auxiliary as q


def get_actor(nombre):
    sus_peliculas = q.get_movies_id(nombre, 
                                      'cast')
    detalles = q.get_peliculas('id', 
                               'return')
    peliculas = pd.merge(sus_peliculas, 
                         detalles, 
                         on='movie_id')
    con_retorno = q.filtrar_con_retorno(peliculas)
    
    cantidad = len(sus_peliculas)
    cantidad_con_retorno = len(con_retorno)
    total = con_retorno['return'].sum().round(2)
    promedio = con_retorno['return'].mean().round(2)
    
    return(cantidad, 
           cantidad_con_retorno, 
           total, 
           promedio)


def get_director(nombre):
    sus_peliculas = q.get_movies_id(nombre, 
                                    'crew')
    sus_peliculas = sus_peliculas.query('job == "Director"')
    sus_peliculas = sus_peliculas['movie_id'].copy()
    detalles = q.get_peliculas('id', 
                               'title', 
                               'release_date', 
                               'return', 
                               'budget', 
                               'revenue')
    peliculas = pd.merge(sus_peliculas, 
                         detalles, 
                         on='movie_id')
    con_retorno = q.filtrar_con_retorno(peliculas)
    
    cantidad = len(sus_peliculas)
    cantidad_con_retorno = len(con_retorno)
    total = con_retorno['return'].sum().round(2)
    con_retorno = q.procesar_peliculas(con_retorno)
    
    return (cantidad, 
            cantidad_con_retorno, 
            total, 
            con_retorno)