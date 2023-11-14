from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/theory')
def theory():
    return 'Integrals'


@app.route('/school_math/linear_equations')
def linear_equations():
    return 'math'


@app.route('/school_math/quadratic_equations')
def linear_equations():
    return 'math'


@app.route('/school_math/systems_of_linear_equations')
def linear_equations():
    return 'math'


@app.route('/higher_math/integrals')
def integrals():
    pass


@app.route('/higher_math/derivatives')
def derivatives():
    pass


@app.route('/higher_math/matrices')
def matrices():
    pass
