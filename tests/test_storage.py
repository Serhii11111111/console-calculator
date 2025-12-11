import unittest
from services.storage_service import JsonStorageService
from datetime import datetime
import os

class TestStorage(unittest.TestCase):
    def setUp(self):
        # Використовуємо окремі файли для тестів
        self.storage = JsonStorageService("test_history.json", "test_errors.json")
        # Чистимо файли перед тестами
        for file in ["test_history.json", "test_errors.json"]:
            if os.path.exists(file):
                os.remove(file)

    def test_save_and_load_result(self):
        timestamp = datetime.now().isoformat()
        self.storage.save_result("2+3", 5, timestamp)
        data = self.storage._load_file("test_history.json")
        self.assertEqual(data[-1]["expression"], "2+3")
        self.assertEqual(data[-1]["result"], 5)
        self.assertEqual(data[-1]["timestamp"], timestamp)

    def test_save_error(self):
        timestamp = datetime.now().isoformat()
        self.storage.save_error("2++3", "Некоректний математичний вираз", timestamp)
        data = self.storage._load_file("test_errors.json")
        self.assertEqual(data[-1]["expression"], "2++3")
        self.assertEqual(data[-1]["error"], "Некоректний математичний вираз")
        self.assertEqual(data[-1]["timestamp"], timestamp)
