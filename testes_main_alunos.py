import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TestCalculadora(unittest.TestCase):

    def teste_calculadora(self):
        # Teste operações básicas
        self.assertEqual(calculadora(2, 3, '+'), 5)
        self.assertEqual(calculadora(5, 3, '-'), 2)
        self.assertEqual(calculadora(4, 3, '*'), 12)
        self.assertEqual(calculadora(6, 3, '/'), 2)
        self.assertEqual(calculadora(10, 3, '%'), 1)
        self.assertEqual(calculadora(2, 3, '^'), 8)

        # Teste divisão por zero
        self.assertTrue(math.isnan(calculadora(5, 0, '/')))
        self.assertTrue(math.isnan(calculadora(5, 0, '%')))

        # Teste operador inválido
        self.assertTrue(math.isnan(calculadora(2, 3, '$')))
        self.assertTrue(math.isnan(calculadora(2, 3, '&')))
        self.assertTrue(math.isnan(calculadora(2, 3, 'invalid')))

        # Teste números de vírgula flutuante
        self.assertAlmostEqual(calculadora(2.5, 1.5, '+'), 4.0)
        self.assertAlmostEqual(calculadora(2.5, 2.5, '*'), 6.25)
        self.assertAlmostEqual(calculadora(5.5, 2.5, '/'), 2.2)

        # Teste números negativos
        self.assertEqual(calculadora(-2, 3, '+'), 1)
        self.assertEqual(calculadora(-2, -3, '*'), 6)
        self.assertEqual(calculadora(-10, -5, '/'), 2)

    def teste_calculadora_v2(self):
        # Teste operações básicas
        self.assertEqual(calculadora_v2(2, 3, '+'), 5)
        self.assertEqual(calculadora_v2(5, 3, '-'), 2)
        self.assertEqual(calculadora_v2(4, 3, '*'), 12)
        self.assertEqual(calculadora_v2(6, 3, '/'), 2)
        self.assertEqual(calculadora_v2(10, 3, '%'), 1)
        self.assertEqual(calculadora_v2(2, 3, '^'), 8)

        # Teste divisão por zero
        self.assertTrue(math.isnan(calculadora_v2(5, 0, '/')))
        self.assertTrue(math.isnan(calculadora_v2(5, 0, '%')))

        # Teste operador inválido
        self.assertTrue(math.isnan(calculadora_v2(2, 3, '$')))
        self.assertTrue(math.isnan(calculadora_v2(2, 3, '&')))
        self.assertTrue(math.isnan(calculadora_v2(2, 3, 'invalid')))

        # Teste números de vírgula flutuante
        self.assertAlmostEqual(calculadora_v2(2.5, 1.5, '+'), 4.0)
        self.assertAlmostEqual(calculadora_v2(2.5, 2.5, '*'), 6.25)
        self.assertAlmostEqual(calculadora_v2(5.5, 2.5, '/'), 2.2)

        # Teste números negativos
        self.assertEqual(calculadora_v2(-2, 3, '+'), 1)
        self.assertEqual(calculadora_v2(-2, -3, '*'), 6)
        self.assertEqual(calculadora_v2(-10, -5, '/'), 2)

    def teste_calculadora_v3(self):
        # Teste operações básicas
        self.assertEqual(calculadora_v3(2, 3, '+'), 5)
        self.assertEqual(calculadora_v3(5, 3, '-'), 2)
        self.assertEqual(calculadora_v3(4, 3, '*'), 12)
        self.assertEqual(calculadora_v3(6, 3, '/'), 2)
        self.assertEqual(calculadora_v3(10, 3, '%'), 1)
        self.assertEqual(calculadora_v3(2, 3, '^'), 8)

        # Teste divisão por zero
        self.assertTrue(math.isnan(calculadora_v3(5, 0, '/')))
        self.assertTrue(math.isnan(calculadora_v3(5, 0, '%')))

        # Teste operador inválido
        self.assertTrue(math.isnan(calculadora_v3(2, 3, '$')))
        self.assertTrue(math.isnan(calculadora_v3(2, 3, '&')))
        self.assertTrue(math.isnan(calculadora_v3(2, 3, 'invalid')))

        # Teste números de vírgula flutuante
        self.assertAlmostEqual(calculadora_v3(2.5, 1.5, '+'), 4.0)
        self.assertAlmostEqual(calculadora_v3(2.5, 2.5, '*'), 6.25)
        self.assertAlmostEqual(calculadora_v3(5.5, 2.5, '/'), 2.2)

        # Teste números negativos
        self.assertEqual(calculadora_v3(-2, 3, '+'), 1)
        self.assertEqual(calculadora_v3(-2, -3, '*'), 6)
        self.assertEqual(calculadora_v3(-10, -5, '/'), 2)

    def teste_calculadora_v4(self):
        # Teste operações básicas
        self.assertEqual(calculadora_v4(2, 3, '+'), 5)
        self.assertEqual(calculadora_v4(5, 3, '-'), 2)
        self.assertEqual(calculadora_v4(4, 3, '*'), 12)
        self.assertEqual(calculadora_v4(6, 3, '/'), 2)
        self.assertEqual(calculadora_v4(10, 3, '%'), 1)
        self.assertEqual(calculadora_v4(2, 3, '^'), 8)

        # Teste divisão por zero
        self.assertTrue(math.isnan(calculadora_v4(5, 0, '/')))
        self.assertTrue(math.isnan(calculadora_v4(5, 0, '%')))

        # Teste operador inválido
        self.assertTrue(math.isnan(calculadora_v4(2, 3, '$')))
        self.assertTrue(math.isnan(calculadora_v4(2, 3, '&')))
        self.assertTrue(math.isnan(calculadora_v4(2, 3, 'invalid')))

        # Teste números de vírgula flutuante
        self.assertAlmostEqual(calculadora_v4(2.5, 1.5, '+'), 4.0)
        self.assertAlmostEqual(calculadora_v4(2.5, 2.5, '*'), 6.25)
        self.assertAlmostEqual(calculadora_v4(5.5, 2.5, '/'), 2.2)

        # Teste números negativos
        self.assertEqual(calculadora_v4(-2, 3, '+'), 1)
        self.assertEqual(calculadora_v4(-2, -3, '*'), 6)
        self.assertEqual(calculadora_v4(-10, -5, '/'), 2)


if __name__ == '__main__':
    unittest.main()



# para correr os testes: python -m unittest -v testes_main_alunos.py
