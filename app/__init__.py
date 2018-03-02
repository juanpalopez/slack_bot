import json
from flask import Flask, request
# from flask_restfull import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
# api = Api(app)
CORS(app)


tensions = ['dummy tension']

@app.route('/', methods=['GET'])
def get_tensions():
    return json.dumps(tensions)


@app.route('/', methods=['POST'])
def add_tensions():
    try:
        tension = (request.form['tension'])
        tensions.append(tension)
    except Exception:
        raise 'oops'
    return json.dumps(tensions)
