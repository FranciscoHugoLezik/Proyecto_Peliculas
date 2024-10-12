import unittest

import src.modules.credits.credits as c


class TestCredits(unittest.TestCase):
    def test_get_actor(self):
        (cantidad, 
         cantidad_con_retorno, 
         retorno_total, 
         retorno_promedio) = c.get_actor('Tom Hanks')
        
        self.assertEqual(cantidad, 71)
        self.assertEqual(cantidad_con_retorno, 41)
        self.assertEqual(retorno_total, 178.85)
        self.assertEqual(retorno_promedio, 4.36)
        
        
    def test_get_director(self):
        (cantidad, 
         cantidad_con_retorno, 
         retorno_total, 
         peliculas) = c.get_director('John Lasseter')
        
        self.assertEqual(cantidad, 9)
        self.assertEqual(cantidad_con_retorno, 4)
        self.assertEqual(retorno_total, 23.81)
        
        self.assertIsInstance(peliculas, list)
        for pelicula in peliculas:
            self.assertIsInstance(pelicula, dict)
            
        self.assertEqual(len(peliculas), 4)
        for pelicula in peliculas:
            self.assertEqual(len(pelicula), 5)
        
        for pelicula in peliculas:
            atributos = tuple(pelicula.keys())
            atributos_buscados = (
                'Titulo', 
                'Fecha_de_estreno', 
                'Retorno', 
                'Presupuesto', 
                'Ganancia'
            )
            estan_los_atributos = True
            for atributo in atributos:
                if atributo not in atributos_buscados:
                    estan_los_atributos = False
                    break
            self.assertTrue(estan_los_atributos)


if __name__ == '__main__':
    unittest.main()