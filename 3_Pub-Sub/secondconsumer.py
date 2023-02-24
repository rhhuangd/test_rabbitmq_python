import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'Secondconsumer: received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

# random queue name
# once the consumer connection is colsed, the queue can be deleted
queue = channel.queue_declare('', exclusive=True)  

# bind the queue to the specified exchange
channel.queue_bind(exchange='pubsub', queue=queue.method.queue) # we don't know the queue name

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print(f'Start Consuming')

channel.start_consuming()