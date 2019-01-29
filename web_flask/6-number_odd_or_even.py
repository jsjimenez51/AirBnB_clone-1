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
@app.route('/python/(<text>)', strict_slashes=False)
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
    Displays a HTML page if n is an integer
    H1 tag: Number n, in the tag BODY
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_template(n):
    '''
    Displays a HTML page if n is an integer
    H1 tag: Number n is even|odd, in the tag BODY
    '''
    this_plate = 'even'
    if n % 2 == 1:
        this_plate = 'odd'
    return render_template('6-number_odd_or_even.html', num=n,
                           evenORodd=this_plate)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
