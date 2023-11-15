#!/usr/bin/python3
"""Starts a Flask web application that gives a return based on route:
'/' returns "Hello HBNB!”
'/hbnb returns "HBNB"
'/c/<text>' returns the value of the variable 'text'
'/python/<text>' returns the value of variable 'text'
'/number/<n>' returns "n is a number"
'/number_template/<n>' displays an HTML if n is an int
'/number_odd_or_even/<n>' displays an HTML file if n is an int
"""
from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp_route(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_route(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
