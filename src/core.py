from src.calculator import Calculator

class App:

    def __init__(self):
        self.__calculator = Calculator()

    def run(self):
        self.__calculator.run()
