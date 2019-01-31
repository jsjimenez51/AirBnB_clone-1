#!/usr/bin/python3
'''
starts a Flask web app
listening on 0.0.0.0, port 5000
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    Displays Hello HBNB if successful
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Displays HBNB if successful
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    Displays the input text with underscores replaced with spaces
    '''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    '''
    Displays python followed by text
    '''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
    Displays n if it is a number
    '''
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    Inserts n as a parameter into an HTML page
    H1 tag: Number n, in the tag BODY
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
