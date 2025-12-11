import unittest
from main import MathController
from datetime import datetime

class TestMathControllerIntegration(unittest.TestCase):
    def setUp(self):
        self.controller = MathController()
        # Використовуємо тестові файли
        self.controller.storage.filename = "test_history.json"
        self.controller.storage.error_filename = "test_errors.json"

    def test_addition(self):
        expr = "2+3"
        result = 5
        timestamp = datetime.now().isoformat()
        self.controller.storage.save_result(expr, result, timestamp)

    def test_invalid_expression(self):
        expr = "2++3"
        timestamp = datetime.now().isoformat()
        self.controller.storage.save_error(expr, "Некоректний математичний вираз", timestamp)

