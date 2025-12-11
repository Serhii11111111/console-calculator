class MathExpression:
    def __init__(self, expression: str, result: float):
        self.expression = expression
        self.result = result

    def to_dict(self):
        return {"expression": self.expression, "result": self.result}
