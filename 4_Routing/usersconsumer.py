import pika
from pika.exchange_type import ExchangeType

def on_message_received(channel, method, properties, body):
    print(f'Users Consumer - Received message: {body}')

connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.exchange_declare('topicExchange', ExchangeType.topic)
queue = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(queue=queue.method.queue, exchange='topicExchange', routing_key='user.#')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print('Start consuming')

channel.start_consuming()