import sys
import os

main_file = os.path.basename(sys.argv[0])

if main_file in ["query.py", "constant.py"]:
    import auxiliary as aux
else:
    from src.scripts import auxiliary as aux


MOVIES = aux.importar_archivo('data', 
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


DIAS = {
    'lunes': 'Monday', 
    'martes': 'Tuesday', 
    'miercoles': 'Wednesday', 
    'jueves': 'Thursday', 
    'viernes': 'Friday', 
    'sabado': 'Saturday', 
    'domingo': 'Sunday'
}