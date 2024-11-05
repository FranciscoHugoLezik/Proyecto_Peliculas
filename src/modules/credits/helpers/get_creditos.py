import pandas as pd

from src.modules.others.import_file import importar_archivo


def get_creditos(nombre: str, 
                 archivo: str) -> pd.DataFrame:
    """Importa un dataset guardado en la 
    carpeta credits (los creditos de las peliculas).
    Filtra los datos de la persona y elimina los 
    duplicados.

    Args:
        persona (str): es el nombre de una persona.
        archivo (str): es el nombre de un archivo.

    Returns:
        pd.DataFrame: contiene los creditos de la 
        persona.
    """
    nombre = nombre.lower()
    dataset = importar_archivo(
        'data', 
        f'{archivo}.parquet'
        )
    sus_creditos = dataset[
        dataset['name'].str.lower() == nombre
        ].copy()
    sus_creditos.drop_duplicates(
        subset=['movie_id'], 
        inplace=True
        )
    return(sus_creditos)