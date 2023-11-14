from flask import Flask, request
from flask import render_template
from sympy import sympify, latex

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/theory')
def theory():
    return 'Integrals'


@app.route('/school_math/linear_equations')
def linear_equations():
    return render_template('in_dev.html', page_name='Линейные уравнения')


@app.route('/school_math/quadratic_equations')
def quadratic_equations():
    return render_template('in_dev.html', page_name='Квадратные уравнения')


@app.route('/school_math/systems_of_linear_equations')
def systems_of_linear_equations():
    return render_template('in_dev.html', page_name='Системы квадратных уравнений')


@app.route('/higher_math/integrals')
def integrals():
    return render_template('higher_math/integrals.html')


@app.route('/generate_integrals', methods=['POST'])
def generate_integrals():
    data = request.form.get('data')
    num_expressions = int(request.form.get('numExpressions', 1))

    try:
        latex_equations = [fr'\int {latex(data)}  \,dx' for _ in range(num_expressions)]

        return render_template('higher_math/integrals.html', latex_equations=latex_equations, error=None)
    except Exception as e:
        return render_template('higher_math/integrals.html', latex_equations=None, error=str(e))


@app.route('/higher_math/derivatives')
def derivatives():
    return render_template('in_dev.html', page_name='Производные')


@app.route('/higher_math/matrices')
def matrices():
    return render_template('in_dev.html', page_name='Матрицы')
