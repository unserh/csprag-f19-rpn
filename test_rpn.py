import unittest
import rpn

# My TestBasics class that inherits from unittest.TestCase
class TestBasics(unittest.TestCase):
    
    def test_add(self):
        result - rpn.calculate('1 1 +')
        self.assertEqual(2, result)
