from typing import List

import pandas as pd


def procesar_peliculas(peliculas: pd.DataFrame) -> List[dict]:
    """Renombra las columnas y modifica los datos de 
    la columna 'Fecha_de_estreno'. Por último, lo 
    convierte en una lista de diccionarios.

    Args:
        peliculas (pd.DataFrame): cada fila es una 
        pelicula.

    Returns:
        list[dict]: cada diccionario es una pelicula.
    """
    peliculas = peliculas[['title', 
                           'release_date', 
                           'return', 
                           'budget', 
                           'revenue']].copy()
    peliculas.rename(columns={'title': 'Titulo', 
                              'release_date': 'Fecha_de_estreno', 
                              'return': 'Retorno', 
                              'budget': 'Presupuesto', 
                              'revenue': 'Ganancia'}, 
                     inplace=True)
    
    peliculas = peliculas.to_dict(orient="records")
    return(peliculas)