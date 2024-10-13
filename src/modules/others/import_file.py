import os
from typing import Tuple

import pandas as pd


def importar_archivo(*args: Tuple[str]) -> pd.DataFrame:
    """Retorna un dataframe extraido de un dataset 
    guardado en la ruta de acceso pasado como tupla.

    Args:
        *args (Tuple[str]): La ultima cadena es el nombre 
        del archivo y el resto son carpetas.
    
    Returns:
        pd.DataFrame: Contiene una tabla.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    file_path = os.path.join(base_dir, 
                             *args)
    
    archivo = pd.read_parquet(file_path)
    
    return(archivo)