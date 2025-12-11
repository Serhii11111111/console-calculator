import datetime

class Logger:
    def __init__(self, filename="calculator.log"):
        self.filename = filename

    def log_error(self, message: str):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"[{time}][Err] {message}\n")
