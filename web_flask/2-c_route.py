#!/usr/bin/python3
'''
starts a Flask web app
listening on 0.0.0.0, port 5000
Routes: /: display "Hello HBNB!"
'''
from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
