import pika


class Client:

    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.queues = ['nlp', 'nlp_response', 'storage', 'storage_response']
        self.nlp_response_str = None

    def analize_nlp_callback(self, method, properties, body):
        print(" [x] Received %r" % body)
        self.channel.stop_consuming()
        self.nlp_response_str = body

    def nlp_response(self):
        self.channel.basic_consume(queue=self.queues[1], on_message_callback=self.analize_nlp_callback, auto_ack=True)
        self.channel.start_consuming()

    def get_nlp_response(self):
        return self.nlp_response

    # The visible method for request a
    def GET_analize_nlp(self, file):
        # Send to rabbit the nlp analize method
        self.channel.basic_publish(exchange='', routing_key=self.queues[0], body=file)
        # Start waiting for the result.
        self.nlp_response()
        return self.get_nlp_response()
