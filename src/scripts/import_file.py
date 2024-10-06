import os

import pandas as pd


def importar_archivo(*args: tuple) -> pd.DataFrame:
    """Retorna un dataframe extraido de un dataset 
    guardado en la ruta de acceso pasado como tupla.

    Args:
        *args (tuple): Es una tupla cuyos elementos 
        son cadenas. La ultima cadena es el nombre 
        del archivo y el resto son carpetas.
    
    Returns:
        pd.DataFrame: Contiene una tabla.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(current_dir))
    file_path = os.path.join(base_dir, 
                             *args)
    
    archivo = pd.read_parquet(file_path, 
                              engine='fastparquet')
    
    return(archivo)