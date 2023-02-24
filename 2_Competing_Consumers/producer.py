import pika
import time
import random

# Basic flow of creating a producer
# 1. establish the connection
# 2. create channels
# 3. create queues
# 4. create messages
# 5. publish the messages
# 6. close the connection

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel_1 = connection.channel()

channel_1.queue_declare(queue='queue1')

messageID = 1

while(True):
    message_1 = f'Sending message ID: {messageID}'
    channel_1.basic_publish(exchange='', routing_key='queue1', body=message_1)
    print(f'sent message: {message_1}')
    time.sleep(random.randint(1,4))
    messageID += 1

# connection.close()