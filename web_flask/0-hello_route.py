#!/usr/bin/python3
"""Starts a Flask web application that returns “Hello HBNB!”"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
