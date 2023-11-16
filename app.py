from flask import Flask, request, send_file, session
from flask import render_template
from dotenv import load_dotenv

import os

from utils.integral import Integral


app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_KEY')


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


# TODO: добавить обработку ошибок
@app.route('/generate_integrals', methods=['POST'])
def generate_integrals():
    data = request.form.get('data')
    constants = request.form.get('constants', '').split(',')
    bounds = list(map(int, request.form.get('bounds', '').split(',')))
    num_expressions = int(request.form.get('numExpressions', 1))

    try:
        session['generate_integrals'] = []
        for _ in range(num_expressions):
            integral = Integral(data, constants).generate_latex_integral_expression(bounds)
            session['generate_integrals'].append(integral)
        return render_template('higher_math/integrals.html', latex_equations=session['generate_integrals'], error=None)
    except Exception as e:
        return render_template('higher_math/integrals.html', latex_equations=None, error=str(e))


# TODO: Конвертировать .tex in .pdf
# TODO: вынести в отдельную функцию.
@app.route('/download', methods=['POST'])
def download_tex():
    try:
        file_format = request.form.getlist('file_format')[0]
        latex_equations = session['generate_integrals']
        tex_content = ""
        for integral in latex_equations:
            tex_content += f'{integral}\\\\\n'

        with open('integrals.tex', 'w') as file:
            file.write(tex_content)
        return send_file('integrals.tex', as_attachment=True, download_name='integrals.tex')

    except Exception as e:
        return str(e)


@app.route('/higher_math/derivatives')
def derivatives():
    return render_template('in_dev.html', page_name='Производные')


@app.route('/higher_math/matrices')
def matrices():
    return render_template('in_dev.html', page_name='Матрицы')
