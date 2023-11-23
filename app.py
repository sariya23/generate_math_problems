from flask import Flask, request, send_file, session, url_for
from flask import render_template
from dotenv import load_dotenv

import os

from common.integral import Integral
from common.create_file import CreateFile


app = Flask(__name__, static_url_path='/static')
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



# TODO: сделать это общей функцией. И для интегралов и для производны и тд и тп.
# TODO: добавить обработку ошибок
@app.route('/generate_integrals', methods=['POST'])
def generate_integrals():
    data = request.get_json()
    pattern = data.get('pattern')
    constants = data.get('constants', '').split(',')
    bounds = list(map(int, data.get('bounds', '').split(',')))
    num_expressions = int(data.get('numExpressions', 1))

    try:
        session['generated_integrals_in_latex']  = []
        session['generateed_integral_in_string'] = []
        for _ in range(num_expressions):
            latex_integral, string_integral = Integral(pattern, constants).generate_latex_and_pure_integral_expression(bounds)
            session['generated_integrals_in_latex'].append(latex_integral)
            session['generateed_integral_in_string'].append(string_integral)
        return {'status': 'ok'}
    except Exception as e:
        return {'error': str(e)}


@app.route('/download', methods=['POST'])
def download_tex():
    try:
        file_format = request.get_json().get('fileFormat')
        tex_content = ""
        create_file = CreateFile(session['generated_integrals_in_latex'])
        create_file.generate_pdf_tex_file_with_expressions(
            file_name='expressions',
            title_for_document='SOLVE IT NOW!!!',
            type_of_expression='integral'
        )

        if file_format == 'pdf':
            response_data = {
                'path': url_for('static', filename='generated_files/expressions.pdf'),
            }
        else:
            response_data = {
                'path': url_for('static', filename='generated_files/expressions.tex'),
            }         
        return response_data

    except FileNotFoundError as e:
        return {'error': 'File not found'}, 404


@app.route('/get_answers', methods=['POST'])
def get_answers():
    try:
        file_format = request.get_json().get('fileFormat')
        answers = []
        
        for integral_expression in session['generateed_integral_in_string']:
            answers.append(f'{Integral.solve_integral(integral_expression)}\n')
        create_file = CreateFile(answers)
        create_file.generate_pdf_tex_file_with_pure_expression(
            file_name='answers',
            title_for_document='ANSWERS !!!'
        )

        if file_format == 'pdf':
            response_data = {
                'path': url_for('static', filename='generated_files/answers.pdf'),
            }
        else:
            response_data = {
                'path': url_for('static', filename='generated_files/answers.tex'),
            }   
        return response_data

    except Exception as e:
        print(str(e))
        return {'error': f'Smth go wrong! {str(e)}'}, 500

@app.route('/higher_math/derivatives')
def derivatives():
    return render_template('in_dev.html', page_name='Производные')


@app.route('/higher_math/matrices')
def matrices():
    return render_template('in_dev.html', page_name='Матрицы')
