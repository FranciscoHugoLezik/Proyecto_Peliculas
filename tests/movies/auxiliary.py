import unittest

import src.modules.movies.auxiliary_movies as aux


class TestAuxiliaryMovies(unittest.TestCase):
    def test_get_meses(self):
        numeros_de_meses = (
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        )
        meses = aux.get_meses()
        meses = tuple(meses.to_list())
        son_meses = True
        for mes in meses:
            if mes not in numeros_de_meses:
                son_meses = False
                break
        self.assertTrue(son_meses)
        
        
    def test_get_numero_mes(self):
        meses = (
            'enero', 
            'febrero', 
            'marzo', 
            'abril', 
            'mayo', 
            'junio', 
            'julio', 
            'agosto', 
            'septiembre', 
            'octubre', 
            'noviembre', 
            'diciembre'
        )
        numero = 0
        for mes in meses:
            numero += 1
            self.assertEqual(aux.get_numero_mes(mes), 
                             numero)


    def test_get_dias(self):
        dias_en_ingles = (
            'Monday', 
            'Tuesday', 
            'Wednesday', 
            'Thursday', 
            'Friday', 
            'Saturday', 
            'Sunday'
        )
        english_days = aux.get_dias()
        english_days = tuple(english_days.to_list())
        son_dias_en_ingles = True
        for day in english_days:
            if day not in dias_en_ingles:
                son_dias_en_ingles = False
                break
        self.assertTrue(son_dias_en_ingles)


    def test_get_dia_en_ingles(self):
        dias_en_español = (
            'lunes', 
            'martes', 
            'miercoles', 
            'jueves', 
            'viernes', 
            'sabado', 
            'domingo'
        )
        dias_en_ingles = (
            'Monday', 
            'Tuesday', 
            'Wednesday', 
            'Thursday', 
            'Friday', 
            'Saturday', 
            'Sunday'
        )
        for (dia_en_español, 
             dia_en_ingles) in zip(dias_en_español, 
                                   dias_en_ingles):
            self.assertEqual(aux.get_dia_en_ingles(dia_en_español), 
                             dia_en_ingles)
        
        
    def test_get_filmacion(self):
        import pandas as pd
        toy_story = aux.get_filmacion('Toy Story')
        self.assertEqual(type(toy_story), 
                         pd.Series)
        self.assertEqual(toy_story['title'], 
                         'Toy Story')


if __name__ == '__main__':
    unittest.main()