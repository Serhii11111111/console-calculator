from services.parser_service import ParserService
from services.validator import Validator
from services.storage_service import JsonStorageService
from datetime import datetime

class MathController:
    def __init__(self):
        self.parser = ParserService()
        self.validator = Validator()
        # Вказуємо два файли: для результатів та для помилок
        self.storage = JsonStorageService("history.json", "errors.json")

    def run(self):
        print("Консольний калькулятор. Введіть 'exit' для виходу.")
        while True:
            expr = input("Введіть математичний вираз: ")
            if expr.lower() in ["exit", "quit", "0"]:
                print("Вихід із програми...")
                break

            # Перевірка валідності виразу
            if not self.validator.validate(expr):
                print("Некоректний математичний вираз")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.storage.save_error(expr, "Некоректний математичний вираз", timestamp)
                continue

            try:
                # Обчислення виразу
                result = self.parser.evaluate(expr)
                print(f"Результат: {result}")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.storage.save_result(expr, result, timestamp)
            except Exception as e:
                print(f"Помилка: {e}")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.storage.save_error(expr, str(e), timestamp)


def main():
    controller = MathController()
    controller.run()


if __name__ == "__main__":
    main()
