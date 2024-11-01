import unittest

from src.modules.credits.helpers.get_creditos import get_creditos
from src.modules.others.constants import MOVIES
from src.modules.credits.helpers.filtrar_con_retorno import filtrar_con_retorno
from src.modules.credits.helpers.procesar_peliculas import procesar_peliculas


class TestsAuxiliaryCredits(unittest.TestCase):
    def test_get_creditos_cast(self):
        tom_hanks = get_creditos(
            'Tom Hanks', 
            'cast')
        columnas = (
            'cast_id', 
            'character', 
            'credit_id', 
            'gender', 
            'person_id', 
            'name', 
            'order', 
            'movie_id'
        )
        estan_las_columnas = True
        for atributo in tom_hanks:
            if atributo not in columnas:
                estan_las_columnas = False
                break
        self.assertTrue(estan_las_columnas)
        
        
    def test_get_creditos_crew(self):
        john_lasseter = get_creditos(
            'John Lasseter', 
            'crew')
        columnas = (
            'credit_id', 
            'department', 
            'gender', 
            'person_id', 
            'job', 
            'name', 
            'profile_path', 
            'movie_id'
        )
        estan_las_columnas = True
        for atributo in john_lasseter:
            if atributo not in columnas:
                estan_las_columnas = False
                break
        self.assertTrue(estan_las_columnas)
        
        
    def test_filtrar_con_retorno(self):
        peliculas_con_retorno = filtrar_con_retorno(MOVIES)
        cantidad = 0
        for retorno in MOVIES['return']:
            if retorno > 0:
                cantidad += 1
        self.assertEqual(len(peliculas_con_retorno), cantidad)
        
        
    def test_procesar_peliculas(self):
        peliculas_a_procesar = MOVIES.head()
        peliculas_procesadas = procesar_peliculas(peliculas_a_procesar)
        atributos_buscados = (
            'Titulo', 
            'Fecha_de_estreno', 
            'Retorno', 
            'Presupuesto', 
            'Ganancia'
        )
        estan_las_columnas = True
        for atributo, _ in peliculas_procesadas[0].items():
            if atributo not in atributos_buscados:
                estan_las_columnas = False
                break
        self.assertTrue(estan_las_columnas)


if __name__ == '__main__':
    unittest.main()