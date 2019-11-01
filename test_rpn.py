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

    def test_bad_input(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')
