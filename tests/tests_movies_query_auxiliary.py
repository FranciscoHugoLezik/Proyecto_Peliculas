import unittest

import src.scripts.movies_query_auxiliary as m


class TestMoviesQueryAuxiliary(unittest.TestCase):
    def test_get_meses(self):
        numeros_de_meses = (
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        )
        meses = m.get_meses()
        meses = tuple(meses.to_list())
        son_meses = True
        for mes in meses:
            if mes not in numeros_de_meses:
                son_meses = False
                break
        self.assertTrue(son_meses)
        
    def test_get_numero_mes(self):
        self.assertEqual(m.get_numero_mes('enero'), 1)
        self.assertEqual(m.get_numero_mes('febrero'), 2)
        self.assertEqual(m.get_numero_mes('marzo'), 3)
        self.assertEqual(m.get_numero_mes('abril'), 4)
        self.assertEqual(m.get_numero_mes('mayo'), 5)
        self.assertEqual(m.get_numero_mes('junio'), 6)
        self.assertEqual(m.get_numero_mes('julio'), 7)
        self.assertEqual(m.get_numero_mes('agosto'), 8)
        self.assertEqual(m.get_numero_mes('septiembre'), 9)
        self.assertEqual(m.get_numero_mes('octubre'), 10)
        self.assertEqual(m.get_numero_mes('noviembre'), 11)
        self.assertEqual(m.get_numero_mes('diciembre'), 12)

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
        english_days = m.get_dias()
        english_days = tuple(english_days.to_list())
        son_dias_en_ingles = True
        for day in english_days:
            if day not in dias_en_ingles:
                son_dias_en_ingles = False
                break
        self.assertTrue(son_dias_en_ingles)

    def test_get_dia_en_ingles(self):
        self.assertEqual(m.get_dia_en_ingles('lunes'), 
                         'Monday')
        self.assertEqual(m.get_dia_en_ingles('martes'), 
                         'Tuesday')
        self.assertEqual(m.get_dia_en_ingles('miercoles'), 
                         'Wednesday')
        self.assertEqual(m.get_dia_en_ingles('jueves'), 
                         'Thursday')
        self.assertEqual(m.get_dia_en_ingles('viernes'), 
                         'Friday')
        self.assertEqual(m.get_dia_en_ingles('sabado'), 
                         'Saturday')
        self.assertEqual(m.get_dia_en_ingles('domingo'), 
                         'Sunday')
        
    def test_get_filmacion(self):
        import pandas as pd
        toy_story = m.get_filmacion('Toy Story')
        self.assertEqual(type(toy_story), pd.Series)
        self.assertEqual(toy_story['title'], 'Toy Story')


if __name__ == '__main__':
    unittest.main()