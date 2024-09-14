import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, 'data', 'movies_dataset', 'movies_ETL.parquet')

movies_df = pd.read_parquet(file_path, engine='fastparquet')


def cantidad_filmaciones_mes(mes):
    months = {
        'Enero': '1', 
        'Febrero': '2', 
        'Marzo': '3', 
        'Abril': '4', 
        'Mayo': '5', 
        'Junio': '6', 
        'Julio': '7', 
        'Agosto': '8', 
        'Septiembre': '9', 
        'Octubre': '10', 
        'Noviembre': '11', 
        'Diciembre': '12'
    }
    mes_num = int(months.get(mes))
    meses_series = movies_df['release_date'].dt.month
    meses_list = meses_series.tolist()
    cantidad = 0
    for m in meses_list:
        if m == mes_num:
            cantidad+=1
    return (cantidad)