if __name__ == "__main__":
    from import_file import importar_archivo
else:
    from src.scripts.import_file import importar_archivo


MOVIES = importar_archivo('data', 
                          'ETL_data', 
                          'movies_dataset', 
                          'movies.parquet')


MESES = {
    'enero': '1', 
    'febrero': '2', 
    'marzo': '3', 
    'abril': '4', 
    'mayo': '5', 
    'junio': '6', 
    'julio': '7', 
    'agosto': '8', 
    'septiembre': '9', 
    'octubre': '10', 
    'noviembre': '11', 
    'diciembre': '12'
}


DIAS_EN_INGLES = {
    'lunes': 'Monday', 
    'martes': 'Tuesday', 
    'miercoles': 'Wednesday', 
    'jueves': 'Thursday', 
    'viernes': 'Friday', 
    'sabado': 'Saturday', 
    'domingo': 'Sunday'
}