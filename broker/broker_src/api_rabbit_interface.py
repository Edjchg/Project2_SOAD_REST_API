import pika

class API_RMQ_interface():
    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.queues = ['nlp', 'nlp_response', 'storage', 'storage_response']

