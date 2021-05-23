import pika
import uuid


class rpcRequester:
    def __init__(self, host='localhost'):
        self.EXCHANGE = "broker"
        self.RESPONSE = "broker_response"
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.queues = ['nlp', 'nlp_response' 'storage']

        self.channel.exchange_declare(exchange=self.EXCHANGE, exchange_type='direct')

        result = self.channel.queue_declare(queue=self.RESPONSE, exclusive=True) #Cola de respuesta.
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


    def GET_nlp_analyze(self, file):


        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=self.EXCHANGE,
            routing_key='nlp_rk',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=file)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

    def GET_storage(self, file):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=self.EXCHANGE,
            routing_key='storage_rk',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=file)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

req = rpcRequester()
print(req.GET_nlp_analyze("asd"))
#print(req.GET_storage("sdfsdfdf"))
req.connection.close()