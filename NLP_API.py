import flask
from flask import jsonify
from NLP_Analyzer import NlpAnalyzer

nlp_api = flask.Flask(__name__)
nlp_api.config["DEBUG"] = False


@nlp_api.route('/nlp/analyze', methods=['GET'])
def compare():
    nlp_analizer = NlpAnalyzer()
    nlp_analizer.init_nlp("english")

    return jsonify(nlp_analizer.find_names())


nlp_api.run()
