from sympy import symbols, latex, sympify, integrate
from random import randint


class Integral:
    def __init__(self, pattern: str, constant_names: list[str], symbol='x'):
        self.pattern = pattern
        self.constant_names = constant_names
        self.symbol = symbols(symbol)

    def __replace_constant_names_to_random_value(self, bounds: list[int]):
        for i, constant in enumerate(self.constant_names):
            self.pattern = self.pattern.replace(constant, str(randint(*bounds)))
        return self.pattern

    def generate_integral_expression(self, bounds: list[int]):
        self.pattern = self.__replace_constant_names_to_random_value(bounds)
        integral = self.pattern
        return integral

    def generate_integral_latex_expression(self, bounds):
        self.pattern = self.__replace_constant_names_to_random_value(bounds)
        return latex(sympify(self.pattern, evaluate=False))

    def generate_latex_and_pure_integral_expression(self, bounds: list[int]):
        self.pattern = self.__replace_constant_names_to_random_value(bounds)
        expression = sympify(self.pattern, evaluate=False)
        latex_integral = latex(expression)
        return latex_integral, self.pattern

    def wrap_expression_in_latex_integral(self, expression: str):
        return fr'\int {latex(expression)}  \,d{self.symbol}'

    @classmethod
    def solve_integral(cls, math_expression: str):
        x = symbols('x')
        print(math_expression)
        expression = sympify(math_expression)

        return latex(integrate(expression, x))

if __name__ == '__main__':
    pass