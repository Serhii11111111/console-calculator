import json
import os

class JsonStorageService:
    def __init__(self, result_file="history.json", error_file="errors.json"):
        self.result_file = result_file
        self.error_file = error_file

    def save_result(self, expression, result, timestamp):
        data = self._load_file(self.result_file)
        data.append({
            "expression": expression,
            "result": result,
            "timestamp": timestamp
        })
        self._save_file(self.result_file, data)

    def save_error(self, expression, error_message, timestamp):
        data = self._load_file(self.error_file)
        data.append({
            "expression": expression,
            "error": error_message,
            "timestamp": timestamp
        })
        self._save_file(self.error_file, data)

    def _load_file(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def _save_file(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)



