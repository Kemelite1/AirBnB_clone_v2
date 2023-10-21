#!/usr/bin/python3
""" A Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """ Print message """
    return 'Hello HBNB!'


@app.route('/hbnb')
def home2():
    """ Print message """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
