from flask import Flask, request, session, url_for
from flask import render_template

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
    pass


@app.route('/higher_math/integrals')
def integrals():
    return render_template('higher_math/integrals.html')


@app.route('/generate_integrals', methods=['POST'])
def generate_integrals():
    data = request.get_json()
    pattern = data.get('pattern')
    constants = data.get('constants', '').split(',')
    bounds = list(map(int, data.get('bounds', '').split(',')))
    num_expressions = int(data.get('numExpressions', 1))

    try:
        session['generated_integrals_in_latex'] = []
        for _ in range(num_expressions):
            latex_integral = Integral(pattern, constants).generate_integral_latex_expression(bounds)
            session['generated_integrals_in_latex'].append(latex_integral)
        return {'status': 'ok'}
    except Exception as e:
        return {'error': str(e)}


@app.route('/download', methods=['POST'])
def download():
    try:
        file_format = request.get_json().get('fileFormat')
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
