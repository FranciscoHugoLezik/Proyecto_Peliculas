import pandas as pd

from src.modules.others.constants import MOVIES


def get_meses() -> pd.Series:
    """Se obtienen los numeros de los meses de 
    la columna 'release date' (fecha de estreno) 
    del dataset MOVIES.

    Returns:
        pd.Series: son los numeros de los meses.
    """
    solo_meses = (
        pd.to_datetime(
            MOVIES['release_date'])
        .dt.month)
    
    return(solo_meses)