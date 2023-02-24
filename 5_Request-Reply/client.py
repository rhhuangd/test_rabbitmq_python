import pika
import uuid

def on_reply_message_received(channel, method, properties, body):
    print(f'Reply received: {body}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

reply_queue = channel.queue_declare('', exclusive=True)
channel.basic_consume(reply_queue.method.queue, auto_ack=True, on_message_callback=on_reply_message_received)

channel.queue_declare(queue='request-queue')
message = 'Can I request a reply?'
cor_id = str(uuid.uuid4())
channel.basic_publish(
    exchange='',
    routing_key='request-queue',
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ),
    body=message
)

print(f'Start Client')
channel.start_consuming()
