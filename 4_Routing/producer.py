import pika
from pika.exchange_type import ExchangeType

connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

# channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='topicExchange', exchange_type=ExchangeType.topic)

# message_1 = 'analytics message'
# message_2 = 'payments message'
# message_3 = 'both messages'

message = "An European user paid for something ++--"

# channel.basic_publish('routing', 'analyticsonly', message_1)
# print(f'Send message: {message_1}')

# channel.basic_publish('routing', 'paymentsonly', message_2)
# print(f'Send message: {message_2}')

# channel.basic_publish('routing', 'both', message_3)
# print(f'Send message: {message_3}')

# channel.basic_publish('topicExchange', 'user.europe.*', message)
channel.basic_publish('topicExchange', '*.payments', message)
# channel.basic_publish('topicExchange', 'user.europe.*', message)
print(f'Send message: {message}')

connection.close()