import logging
import os
import urllib

from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/hello')
def hello_world():
    return jsonify('Hello world')


@app.route('/api/hello2')
def next_func():
    return jsonify("Another example of a call to Flask.")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
