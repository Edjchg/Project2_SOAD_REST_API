# Pulling an image with python 3
FROM python:3.8-slim-buster
# Setting the working directory
WORKDIR nlp_analyzer/
# ------------Installing some dependencies------------
# - Flask:
RUN pip install flask
# - PyPDF4
RUN pip install PyPDF4
# - Spacy and the model
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python3 -m spacy download en_core_web_sm
# ------------Creating two directories----------------
RUN mkdir nlp
RUN mkdir tmp_files
# ------------Copying the local directories to the----
# ------------container-------------------------------
COPY nlp nlp
COPY tmp_files tmp_files
# ------------Changing the working directory----------
WORKDIR nlp/
# ------------Executing the API-----------------------
CMD ["python3", "NLP_API.py"]
# ------------Some commands---------------------------
# Execute this Dockerfile:
# - sudo docker build -t test/nlpapi:1.0 .  -> it will create a number at the end: copy it.
# - sudo docker run --publish 5000:5000 <paste the number copied before>   ->the first port will be the exposed,
# and the second one is the default by the API.
# sudo docker run -it <paste the number copied before> bash  -> will show a console where we can explore the container.

# References:
# - https://www.youtube.com/watch?v=gAkwW2tuIqE
# - https://docs.docker.com/language/python/build-images/


# Some commands:

# Delete images:
#    $ sudo docker rmi -f <IMAGE ID>
# Watch images:
#    $ sudo docker images
# Watch all containers:
#    $ sudo docker ps -a
# Stop containers:
#    $ sudo docker stop <CONTAINER ID>
# Delete containers:
#    $ sudo docker rm <CONTAINER ID>