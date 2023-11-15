from sympy import symbols, latex
from random import randint


class Integral:
    def __init__(self, pattern: str, *constant_names, symbol='x'):
        self.pattern = pattern
        self.constant_names = constant_names
        self.symbol = symbols(symbol)

    def __replace_constant_names_to_random_value(self, bounds: list[int]):
        for i, constant in enumerate(self.constant_names):
            self.pattern = self.pattern.replace(constant, str(randint(*bounds)))
        return self.pattern

    def generate_integral_expression(self, bounds: list[int]):
        self.__replace_constant_names_to_random_value(bounds)
        integral = fr'\int {latex(self.pattern)}  \,d{self.symbol}'
        return integral


if __name__ == '__main__':
    a = Integral('a*x', 'a')
    print(a.generate_integral_expression([1, 100]))