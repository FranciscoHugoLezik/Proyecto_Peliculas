if __name__ == "__main__":
    import movies_query_auxiliary as d
else:
    from src.scripts import movies_query_auxiliary as q


def cantidad_filmaciones_mes(mes):
    meses = q.get_meses()
    cantidades = meses.value_counts()
    numero_mes = q.get_numero_mes(mes)
    cantidad = int(cantidades[numero_mes])
    
    return (cantidad)


def cantidad_filmaciones_dia(dia):   
    dias = q.get_dias()
    cantidades = dias.value_counts()
    dia_en_ingles = q.get_dia_en_ingles(dia)
    cantidad = int(cantidades[dia_en_ingles])
    
    return (cantidad)


def score_titulo(titulo):
    filmacion = q.get_filmacion(titulo)
    año = int(filmacion['release_year'])
    popularidad = float(filmacion['popularity'])
    
    return (año, 
            popularidad)


def votos_titulo(titulo): 
    filmacion = q.get_filmacion(titulo)
    año = int(filmacion['release_year'])
    cantidad = int(filmacion['vote_count'])
    promedio = float(filmacion['vote_average'])
    
    return (año, 
            cantidad, 
            promedio)