import unittest
from services.validator import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_valid_expression(self):
        self.assertTrue(self.validator.validate("2+3*4"))

    def test_invalid_expression_double_operator(self):
        self.assertFalse(self.validator.validate("2++3"))

    def test_invalid_characters(self):
        self.assertFalse(self.validator.validate("2+3a"))
