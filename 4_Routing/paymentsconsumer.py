import pika
from pika.exchange_type import ExchangeType

def on_message_received(channel, method, properties, body):
    print(f'Payments Consumer - Received message: {body}')

connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

# channel.exchange_declare('routing', ExchangeType.direct)
channel.exchange_declare('topicExchange', ExchangeType.topic)
queue = channel.queue_declare(queue='', exclusive=True)
# channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key="paymentsonly")
# channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key="both")
channel.queue_bind(exchange='topicExchange', queue=queue.method.queue, routing_key='#.payments')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print('Start consuming')

channel.start_consuming()