#!/usr/bin/python3
"""Starts a Flask web application that gives a return based on route:
'/' returns "Hello HBNB!”
'/hbnb returns "HBNB"
/c returns the value of the variable 'text'
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
