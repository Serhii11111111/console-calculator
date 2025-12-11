from services.parser_service import ParserService
from services.validator import Validator
from services.storage_service import JsonStorageService

class MathController:
    def __init__(self):
        self.parser = ParserService()
        self.validator = Validator()
        self.storage = JsonStorageService("history.json")  # файл для історії

    def run(self):
        print("Консольний калькулятор. Введіть 'exit' для виходу.")
        while True:
            expr = input("Введіть математичний вираз: ")
            if expr.lower() in ["exit", "quit", "0"]:
                break

            if not self.validator.validate(expr):
                print("Некоректний математичний вираз")
                self.storage.save_error(expr, "Некоректний математичний вираз")
                continue

            try:
                result = self.parser.evaluate(expr)
                print(f"Результат: {result}")
                self.storage.save(expr, result)
            except Exception as e:
                print(f"Помилка: {e}")
                self.storage.save_error(expr, str(e))

