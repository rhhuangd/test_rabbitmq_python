import pika

# 1. establish the connection
# 2. create channels
# 3. create queues
# 4. binding callback functions with message-received events of consumers + binding consumers to channels 
# 4. start consuming (channels)

def on_message_received(channel, method, properties, body):
    print(f'message consumed => {body}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel_1 = connection.channel()
channel_2 = connection.channel()

channel_1.queue_declare(queue='queue1')
channel_2.queue_declare(queue='queue2')

channel_1.basic_consume(queue='queue1', auto_ack=True, on_message_callback=on_message_received)
channel_2.basic_consume(queue='queue2', auto_ack=True, on_message_callback=on_message_received)

print('starting consuming')

channel_1.start_consuming()
channel_2.start_consuming()