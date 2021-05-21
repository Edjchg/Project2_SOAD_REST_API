FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR storage_api/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "storage_api.py"]

