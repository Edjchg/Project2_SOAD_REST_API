import json

import flask
from flask import jsonify, request
from NLP_Analyzer import NlpAnalyzer
from Person import Person

nlp_api = flask.Flask(__name__)
nlp_api.config["DEBUG"] = False



@nlp_api.route('/', methods=['GET'], strict_slashes=False)
def hello_from_nlp():
    return "Hello from NLP REST API, http://127.0.0.1:5000/nlp/analyze?file=textoprueba.txt"


@nlp_api.route('/nlp/analyze', methods=['GET'], strict_slashes=False)
def analyze_file():
    if 'file' in request.args:
        file = request.args['file']
        nlp_analizer = NlpAnalyzer()
        nlp_analizer.init_nlp("english")
        jsonStr = json.dumps([Person.__dict__ for Person in nlp_analizer.analyze_file(file)])
        return jsonify(jsonStr)
    else:
        return "No file declaration"


@nlp_api.route('/nlp/compare', methods=['GET'], strict_slashes=False)
def compare_mongo():
    return "Compare"


@nlp_api.route('/nlp/delete', methods=['GET'], strict_slashes=False)
def delete_file():
    if 'file' in request.args:
    	nlp_analizer = NlpAnalyzer()
        file = request.args['file']
        nlp_analizer.delete_file(file)
        return "File deleted"
    else:
        return "No file declaration"


nlp_api.run(host='0.0.0.0')

# http://127.0.0.1:5000/nlp/analyze?file=textoprueba.txt
