FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR nlp/

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python3 -m spacy download es_core_news_sm
RUN python3 -m spacy download en_core_web_sm

COPY . .

CMD ["python3", "NLP_API.py"]