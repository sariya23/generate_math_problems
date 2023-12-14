from sympy import symbols, latex, sympify, integrate
from random import randint

from common.bounds import Bounds


class Integral:
    def __init__(self, pattern: str, constant_names: list[str], symbol='x'):
        self.pattern = pattern
        self.constant_names = constant_names
        self.symbol = symbols(symbol)

    def __replace_constant_names_to_random_value(self, bounds: Bounds) -> str:
        for i, constant in enumerate(self.constant_names):
            self.pattern = self.pattern.replace(constant, str(randint(bounds.start_value, bounds.end_value)))
        return self.pattern

    def generate_integral_latex_expression(self, bounds: Bounds) -> str:
        self.pattern = self.__replace_constant_names_to_random_value(bounds)
        expression = sympify(self.pattern, evaluate=False)
        return latex(sympify(expression, evaluate=False))
