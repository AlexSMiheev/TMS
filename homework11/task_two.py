class WorkingWithText:
    def __init__(self, string: str):
        self.string = string

    def upper_text(self):
        return self.string.upper()


lower_string = WorkingWithText('Hello world')
print(lower_string.upper_text())
