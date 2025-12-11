import re

class Validator:
    def __init__(self):
        # регулярка для базових арифметичних виразів
        self.pattern = r'^[\d\s\+\-\*\/\(\)]+$'

    def validate(self, expression):
        # тільки допустимі символи
        if not re.match(self.pattern, expression):
            return False
        # не допускаємо подвійні оператори
        if re.search(r'[\+\-\*\/]{2,}', expression):
            return False
        # перевірка збалансованості дужок
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False
        return True

