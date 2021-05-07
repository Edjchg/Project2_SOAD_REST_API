import io
import os
import PyPDF4
import spacy


# Tutorial https://stackabuse.com/python-for-nlp-parts-of-speech-tagging-and-named-entity-recognition/

# installing en_core_web_sm(english): conda install -c conda-forge spacy-model-en_core_web_sm
# installing es_core_news_sm(spanish): conda install -c conda-forge spacy-model-es_core_news_sm
#                                      conda install -c conda-forge/label/cf202003 spacy-model-es_core_news_sm
#                                      python -m spacy download es_core_news_sm


class NlpAnalyzer:
    def __init__(self):
        self.nlp = None

    def init_nlp(self, language):
        if language == "english":
            self.nlp = spacy.load('en_core_web_sm')
        else:
            self.nlp = spacy.load('es_core_news_sm')

    def find_names(self, line):
        # sen = self.nlp(u'Manchester United is looking to sign Edgar Chaves and Kane for $90 million')
        entity_set = self.nlp(line)
        result = []
        for entity in entity_set.ents:
            if entity.label_ == "PERSON":
                result.append(entity.text)
        return result

    def analyze_file(self, file):
        file = "tmp_files/"+file
        if os.path.exists(file):
            _, file_extension = os.path.splitext(file)
            file_to_analyze = open(file, 'r')
            if file_extension == ".txt":
                lines = file_to_analyze.readlines()
                for line in lines:
                    print(self.find_names(line))
            elif file_extension == ".pdf":
                pdf_file = open(file, 'rb')
                pdf_reader = PyPDF4.PdfFileReader(pdf_file)
                for i in range(pdf_reader.getNumPages()):
                    page = pdf_reader.getPage(i).extractText().split(",")
                    for line in page:
                        print(self.find_names(line))
            return "Finished"
        else:
            return "This file does not exists."

    def delete_file(self, file):
        file = "tmp_files/"+file
        if os.path.exists(file):
            os.remove(file)
            return "File deleted"
        else:
            return "The file does not exist"


nlp_analizer = NlpAnalyzer()
nlp_analizer.init_nlp("english")
nlp_analizer.analyze_file("textoprueba.txt")
nlp_analizer.delete_file("README.md")
