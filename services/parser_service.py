import re

class ParserService:
    def evaluate(self, expression: str):
        """Обчислює математичний вираз, кидає ValueError для некоректного"""
        # Валідація подвійних операторів (++, --, +- тощо)
        if re.search(r'(\+\+|--|\+-|-\+|\*\*|//|[^\d\+\-\*/\(\)\s])', expression):
            raise ValueError("Некоректний математичний вираз")
        try:
            # eval безпечніше через обмеження на allowed chars
            allowed_chars = "0123456789+-*/(). "
            if any(c not in allowed_chars for c in expression):
                raise ValueError("Некоректний математичний вираз")
            result = eval(expression)
            return result
        except Exception:
            raise ValueError("Некоректний математичний вираз")
