#!/usr/bin/python3
"""Starts a Flask web application that gives a return based on route:
'/' returns "Hello HBNB!”
'/hbnb returns "HBNB"
'/c/<text>' returns the value of the variable 'text'
'/python/<text>' returns the value of variable 'text'
'/number/<n>' returns "n is a number"
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text_cp = text.replace('_', ' ')
    return "C {}".format(text_cp)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text='is cool'):
    text_cp = text.replace('_', ' ')
    return "Python {}".format(text_cp)


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
