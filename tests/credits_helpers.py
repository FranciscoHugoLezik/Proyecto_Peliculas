import unittest

from src.modules.others.constants import MOVIES
from src.modules.credits.helpers.get_creditos import get_creditos
from src.modules.credits.helpers.filtrar_con_retorno import filtrar_con_retorno
from src.modules.credits.helpers.procesar_peliculas import procesar_peliculas


class TestsAuxiliaryCredits(unittest.TestCase):
    def test_get_creditos_cast(self):
        tom_hanks = get_creditos(
            'Tom Hanks', 
            'cast')
        atributos_buscados = {
            'movie_id', 
            'character', 
            'name'}
        atributos_tom_hanks = set(tom_hanks.columns)
        self.assertTrue(
            atributos_buscados == atributos_tom_hanks)
        
        
    def test_get_creditos_crew(self):
        john_lasseter = get_creditos(
            'John Lasseter', 
            'crew')
        atributos_buscados = {
            'movie_id', 
            'department', 
            'job', 
            'name'}
        atributos_john_lasseter = set(john_lasseter.columns)
        self.assertTrue(
            atributos_buscados == atributos_john_lasseter)
        
        
    def test_filtrar_con_retorno(self):
        peliculas_con_retorno = filtrar_con_retorno(MOVIES)
        cantidad = 0
        for retorno in MOVIES['return']:
            if retorno > 0:
                cantidad += 1
        self.assertEqual(
            len(peliculas_con_retorno), 
            cantidad)
        
        
    def test_procesar_peliculas(self):
        peliculas_a_procesar = MOVIES.head()
        peliculas_procesadas = procesar_peliculas(peliculas_a_procesar)
        atributos_buscados = {
            'Titulo', 
            'Fecha_de_estreno', 
            'Retorno', 
            'Presupuesto', 
            'Ganancia'}
        atributos_peliculas_procesadas = set(peliculas_procesadas[0].keys())
        self.assertTrue(
            atributos_buscados == atributos_peliculas_procesadas)


if __name__ == '__main__':
    unittest.main()