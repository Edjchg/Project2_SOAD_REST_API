import pika

# Conectar con rabbit.
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# Declarando colas.
channel.queue_declare(queue='hello')
channel.queue_declare(queue='hello_server_response')
json = "{hola:hola}"
# mandando el mensaje:
channel.basic_publish(exchange='', routing_key='hello', body=json)
print(" [x] Sent 'Hello World!'")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    channel.stop_consuming()


channel.basic_consume(queue='hello_server_response', on_message_callback=callback, auto_ack=True)
# esperando respuesta.
channel.start_consuming()

connection.close()

'''
import sys

print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv[1])))'''
