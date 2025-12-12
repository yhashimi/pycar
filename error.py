class ErrorHandler:
    def __init__(self):
        self.last_error = None

    def register(self, message):
        self.last_error = message
        print("[ERROR]", message)

    def get_last_error(self):
        return self.last_error
