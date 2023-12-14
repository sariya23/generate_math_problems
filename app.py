from flask import Flask, request, session, url_for
from flask import render_template

import os

from common.integral import Integral
from common.create_file import CreateFile
from utils import get_bounds_for_generated_constants


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
    form_data = request.get_json()
    pattern_generate = form_data.get('pattern')
    constant_names = form_data.get('constants', '').split(',')
    start_end_generate_constant_values = form_data.get('bounds', '')
    bounds = get_bounds_for_generated_constants(start_end_generate_constant_values)
    amount_of_expression = int(form_data.get('numExpressions', 1))

    try:
        session['generated_integrals_in_latex'] = []
        for _ in range(amount_of_expression):
            latex_integral = Integral(pattern_generate, constant_names).generate_integral_latex_expression(bounds)
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
