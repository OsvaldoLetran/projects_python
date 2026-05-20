import unittest
from func_maths import Calculator


class BlackBoxTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    #TEST DRIVEN DEVELOPMENT
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = self.calc.addition(num_1, num_2)
        self.assertEqual(resultado, 15)    #verificamos que nuestro codigo sea correcto

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = self.calc.addition(num_1, num_2)
        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()