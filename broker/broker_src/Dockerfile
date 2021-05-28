
FROM python:3.8-slim-buster
RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp &
WORKDIR broker_src/

USER root
RUN pip install requests
RUN pip install pika
ENV PYTHONUNBUFFERED=1
COPY . .
CMD ["apt-get", "install", "inetutils-ping"]
CMD ["python3", "rpcReciever.py"]

#sudo docker-compose up --build

#sudo docker container prune -> elimina todos los contenedores.
#sudo docker stop <container id>
#sudo docker rmi -f $(sudo docker images -q)
#http://localhost:15672
