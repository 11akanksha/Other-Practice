def add(a, b):
    return a+b


def sub(a, b):
    return a-b


PI = 3.141


class Speak:
    def __init__(self, stmt):
        self.stmt = stmt

    def say(self):
        print(self.stmt)
