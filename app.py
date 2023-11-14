from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/math')
def math():
    return 'math'


@app.route('/math/integrals')
def integrals():
    return 'Integrals'