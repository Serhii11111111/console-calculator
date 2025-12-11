import unittest
from services.parser_service import ParserService

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = ParserService()

    def test_simple_addition(self):
        self.assertEqual(self.parser.evaluate("2+3"), 5)

    def test_complex_expression(self):
        self.assertEqual(self.parser.evaluate("2+3*4"), 14)

    def test_parentheses(self):
        self.assertEqual(self.parser.evaluate("(2+3)*4"), 20)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.parser.evaluate("2++3")

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.parser.evaluate("2/0")

