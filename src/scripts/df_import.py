import os

import pandas as pd


def importar_archivo(*args):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(current_dir))
    file_path = os.path.join(base_dir, 
                             *args)
    
    archivo = pd.read_parquet(file_path, 
                              engine='fastparquet')
    
    return(archivo)