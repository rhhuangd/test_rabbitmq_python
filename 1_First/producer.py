import pika

# 1. establish the connection
# 2. create channels
# 3. create queues
# 4. create messages
# 5. publish the messages
# 6. close the connection

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel_1 = connection.channel()
channel_2 = connection.channel()

channel_1.queue_declare(queue='queue1')
channel_2.queue_declare(queue='queue2')

message_1 = 'first message'
message_2 = 'second message'

channel_1.basic_publish(exchange='', routing_key='queue1', body=message_1)
channel_2.basic_publish(exchange='', routing_key='queue2', body=message_2)

print(f'sent message => channel_1 with {message_1}, channel_2 with {message_2}')

connection.close()