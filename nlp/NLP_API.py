import flask
from flask import jsonify, request
from NLP_Analyzer import NlpAnalyzer

nlp_api = flask.Flask(__name__)
nlp_api.config["DEBUG"] = False

@nlp_api.route('/', methods=['GET'])
def hello_from_nlp():
    return "Hello from NLP REST API, http://127.0.0.1:5000/nlp/analyze?file=textoprueba.txt"

@nlp_api.route('/nlp/analyze', methods=['GET'])
def analyze_file():
    if 'file' in request.args:
        file = request.args['file']
        nlp_analizer = NlpAnalyzer()
        nlp_analizer.init_nlp("english")

        return jsonify(nlp_analizer.analyze_file(file))
    else:
        return "No file"


nlp_api.run()

# http://127.0.0.1:5000/nlp/analyze?file=textoprueba.txt