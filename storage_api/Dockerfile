FROM python:3.8-slim-buster

# ------------Exposing port------------
EXPOSE 5000

WORKDIR storage_api/

# ------------Installing dependencies------------

#RUN pip install flask
#RUN pip install azure-storage-blob

COPY requirements.txt .
RUN pip install -r requirements.txt
# ------------Creating two directories----------------
#RUN mkdir storage_api
#RUN mkdir tempfile

# ------------Copying the local directories to the----
# ------------container-------------------------------
#COPY storage_api storage_api
COPY . .

# ------------Changing the working directory----------
#WORKDIR storage_api/

# ------------Executing the API-----------------------
CMD ["python3", "storage_api.py"]

# Execute this Dockerfile:
# - sudo docker build -t test/storage_api:1.0 .
# - sudo docker run --publish 5000:5000 <paste the number copied before>