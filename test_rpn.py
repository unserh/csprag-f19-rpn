import unittest
import rpn

# My TestBasics class that inherits from unittest.TestCase
class TestBasics(unittest.TestCase):
    
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate('3 2 -')
        self.assertEqual(1, result)

    def test_multiplication(self):
        result = rpn.calculate('3 6 *')
        self.assertEqual(18, result)

    def test_division_1(self):
        result = rpn.calculate('8 5 /')
        self.assertEqual(1, result)

    def test_division_2(self):
        result = rpn.calculate('8 4 /')
        self.assertEqual(2, result)

    def test_power(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)


    def test_bad_input(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')
