from flask import Flask, request, send_file, session, url_for
from flask import render_template
from dotenv import load_dotenv

import os

from utils.integral import Integral


app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_KEY')
app.static_folder = 'static'

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
    data = request.get_json()
    pattern = data.get('pattern')
    constants = data.get('constants', '').split(',')
    bounds = list(map(int, data.get('bounds', '').split(',')))
    num_expressions = int(data.get('numExpressions', 1))

    try:
        session['generate_integrals'] = []
        for _ in range(num_expressions):
            integral = Integral(pattern, constants).generate_latex_integral_expression(bounds)
            session['generate_integrals'].append(integral)
        return session['generate_integrals']
    except Exception as e:
        return render_template('higher_math/integrals.html', latex_equations=None, error=str(e))


@app.route('/download', methods=['POST'])
def download_tex():
    try:
        file_format = request.get_json().get('fileFormat')
        latex_equations = session['generate_integrals']
        tex_content = ""
        for integral in latex_equations:
            tex_content += f'{integral}\\\\\n'

        with open('static/generated_files/integrals.tex', 'w') as file:
            file.write(tex_content)
        response_data = {
            'path': url_for('static', filename='generated_files/integrals.tex'),
            'extension': 'tex',
        }
        return response_data

    except Exception as e:
        return {'error': 'File not found'}, 404


@app.route('/higher_math/derivatives')
def derivatives():
    return render_template('in_dev.html', page_name='Производные')


@app.route('/higher_math/matrices')
def matrices():
    return render_template('in_dev.html', page_name='Матрицы')
