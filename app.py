from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/school_math')
def school_math():
    return 'math'


@app.route('/theory')
def theory():
    return 'Integrals'


@app.route('/higher_math/integrals')
def integrals():
    pass


@app.route('/higher_math/derivatives')
def derivatives():
    pass

@app.route('/higher_math/matrices')
def matrices():
    pass