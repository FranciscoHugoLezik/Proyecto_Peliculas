import pandas as pd


def filtrar_con_retorno(peliculas: pd.DataFrame) -> pd.DataFrame:
    """Filtra las peliculas cuyo return es 
    mayor de cero.

    Args:
        peliculas (pd.DataFrame): cada fila es una 
        pelicula.

    Returns:
        pd.DataFrame: solo tiene peliculas que 
        cumplen con el filtro.
    """
    con_retorno = peliculas[peliculas['return'] > 0]
    return(con_retorno)