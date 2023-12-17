from test_backend import get_sentence
from flask import Flask, request, render_template
from flask_restful import Api, Resource, abort
import json

app = Flask(__name__)
api = Api(app)

@app.route('/get_sentence/<string:letters>')
def get_sentence(letters: str):
    letters_dict = json.loads(letters)
    return {'data': get_sentence(letters_dict)}

@app.route('/')
def set_up_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)