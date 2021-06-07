import pika


# https://www.rabbitmq.com/tutorials/tutorial-four-python.html
import requests
import json

class rpcReciever:
    def __init__(self, host='localhost'):
        self.host = host
        self.EXCHANGE = 'broker'

        self.connection = None

        self.channel = None
        self.queues = ['nlp', 'storage']
        self.routing_keys = ['nlp_rk', 'storage_rk']
        self.functions = {
            'nlp': self.nlp_callback,
            'storage': self.storage_callback
        }

    def nlp_callback(self, ch, method, props, body):
        # Proceso
        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id= \
                                                             props.correlation_id),
                         body="Hello from NLP")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(body)

    def storage_callback(self, ch, method, props, body):
        # Api
        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body="Hello from Storage")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(body)

    def listen(self):
        # Connecting routing keys with queues

        for i in range(0, len(self.queues)):
            pass
            # self.channel.queue_declare(queue=self.routing_keys[i])
            self.channel.queue_declare(queue=self.queues[i])
            self.channel.queue_bind(exchange=self.EXCHANGE, queue=self.queues[i], routing_key=self.routing_keys[i])
            self.channel.basic_consume(queue=self.queues[i], on_message_callback=self.functions[self.queues[i]])

        # self.channel.basic_qos(prefetch_count=2)
        # for j in range(0, len(self.queues)):
        # self.channel.basic_consume(queue='nlp', on_message_callback=self.nlp_callback)
        # self.channel.basic_consume(queue='storage', on_message_callback=self.storage_callback)

        print("Start listening")
        self.channel.start_consuming()

    def get_connection(self):
        flag = False
        try:

            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
            if self.connection.is_open:
                self.channel = self.connection.channel()
                self.channel.exchange_declare(exchange=self.EXCHANGE, exchange_type='direct')
                flag = True
        except:
            flag = False

        return flag


ser = rpcReciever('172.19.0.2')
response = requests.get("http://172.19.0.2:15672/#/queues")
print(response.status_code)
print(response)
print("Waiting for the server to start")
while not ser.get_connection():
    pass
ser.listen()
