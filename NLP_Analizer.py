import spacy
import flask

# Tutorial https://stackabuse.com/python-for-nlp-parts-of-speech-tagging-and-named-entity-recognition/

sp = spacy.load('en_core_web_sm')

sen = sp(u'Manchester United is looking to sign Harry Kane for $90 million')

print(sen.ents)