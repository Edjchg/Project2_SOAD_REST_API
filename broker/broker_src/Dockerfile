#FROM python:3.8-slim-buster
#FROM rabbitmq:3.7-management
#FROM rabbitmq:3-management-alpine
FROM python:3.8-slim-buster
#RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp &
#EXPOSE 5672
#EXPOSE 15672
WORKDIR broker_src/

USER root

#RUN apt install rabbitmq-server
#RUN service rabbitmq-server restart
#RUN apt-get install python-pip
RUN pip install pika
COPY . .

CMD ["python3", "rpcReciever.py"]

#sudo docker-compose up --build

#sudo docker container prune -> elimina todos los contenedores.
#sudo docker stop <container id>
#sudo docker rmi -f $(sudo docker images -q)
#http://localhost:15672
