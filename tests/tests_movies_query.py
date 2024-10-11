import unittest

import src.scripts.movies.movies as m


class TestMoviesQuery(unittest.TestCase):
    def test_cantidad_filmaciones_mes(self):
        cantidad_enero = m.cantidad_filmaciones_mes('enero')
        self.assertEqual(cantidad_enero, 
                         5912)
        
    def test_cantidad_filmaciones_dia(self):
        cantidad_lunes = m.cantidad_filmaciones_dia('lunes')
        self.assertEqual(cantidad_lunes, 
                         3503)
    
    def test_score_titulo(self):
        (año, 
         popularidad) = m.score_titulo('Toy Story')
        
        self.assertEqual(año, 
                         1995)
        self.assertEqual(popularidad, 
                         21.95)
        
    def test_votos_titulo(self):
        (año, 
         cantidad_votos, 
         promedio_votos) = m.votos_titulo('Toy Story')
        
        self.assertEqual(año, 
                         1995)
        self.assertEqual(cantidad_votos, 
                         5415)
        self.assertEqual(promedio_votos, 
                         7.7)


if __name__ == '__main__':
    unittest.main()