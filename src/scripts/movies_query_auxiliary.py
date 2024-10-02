if __name__ == "__main__":
    import constants as c
else:
    from src.scripts import constants as c
    

def get_meses():
    solo_meses = c.MOVIES['release_date'].dt.month
    
    return(solo_meses)


def get_numero_mes(mes):
    numero_de_mes = int(c.MESES.get(mes))
    
    return(numero_de_mes)


def get_dias():
    solo_dias = c.MOVIES['release_date'].dt.strftime('%A')
    
    return(solo_dias)


def get_dia_en_ingles(dia):
    dia_en_ingles = c.DIAS_EN_INGLES.get(dia)
    
    return(dia_en_ingles)


def get_filmacion(titulo):
    movies = c.MOVIES.copy()
    movies.set_index('title', 
                     inplace=True)
    filmación = movies.loc[titulo]
    
    return(filmación)