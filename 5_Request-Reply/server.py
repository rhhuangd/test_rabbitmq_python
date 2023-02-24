import pika

def on_request_message_received(ch, method, properties, body):
    print(f'Request received: {properties.correlation_id}')
    reply_to_request(ch, properties)   

def reply_to_request(ch, properties):
    ch.basic_publish(exchange='', routing_key=properties.reply_to, body=f'This is a reply to the request {properties.correlation_id}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='request-queue')
channel.basic_consume(queue='request-queue', auto_ack=True, on_message_callback=on_request_message_received)

print(f'Starting Server')
channel.start_consuming()