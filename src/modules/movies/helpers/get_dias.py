import pandas as pd

from src.modules.others.constants import MOVIES


def get_dias() -> pd.Series:
    """Se obtienen los dias en ingles de la 
    columna 'release date' (fecha de estreno) 
    del dataset MOVIES.

    Returns:
        pd.Series: son los dias en ingles.
    """
    solo_dias = (
        pd.to_datetime(
            MOVIES['release_date'])
        .dt.strftime('%A'))
    
    return(solo_dias)