import json

import spacy
import flask

# Tutorial https://stackabuse.com/python-for-nlp-parts-of-speech-tagging-and-named-entity-recognition/

# installing en_core_web_sm(english): conda install -c conda-forge spacy-model-en_core_web_sm
# installing es_core_news_sm(spanish): conda install -c conda-forge spacy-model-es_core_news_sm
#                                      conda install -c conda-forge/label/cf202003 spacy-model-es_core_news_sm
#                                      python -m spacy download es_core_news_sm
from flask import jsonify
from spacy.lang.es.examples import sentences


class NlpAnalyzer:
    def __init__(self):
        self.nlp = None

    def init_nlp(self, language):
        if language == "english":
            self.nlp = spacy.load('en_core_web_sm')
        else:
            self.nlp = spacy.load('es_core_news_sm')

    def find_names(self):
        sen = self.nlp(u'Manchester United is looking to sign Edgar Chaves and Kane for $90 million')
        result = []
        for entity in sen.ents:
            if entity.label_ == "PERSON":
                print(entity.text)
                result.append(entity.text)
        print(result)
        return result


nlp_api = flask.Flask(__name__)
nlp_api.config["DEBUG"] = False


@nlp_api.route('/nlp/analyze', methods=['GET'])
def compare():
    nlp_analizer = NlpAnalyzer()
    nlp_analizer.init_nlp("english")

    return jsonify(nlp_analizer.find_names())

nlp_api.run()

'''
nlp_analizer = NlpAnalyzer()
nlp_analizer.init_nlp("english")

nlp_analizer.find_names()'''
