import json

from kafka import KafkaProducer

# from main import *

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

print('Pushing test events')

users = [
    {'account_id': 'kjduebvfds', 'email': 'marius.something@gmail.cob', 'name': 'Marius',
     '__faust': {'ns': 'inno.main.RegisteredUser'}}
]


for user in users:
    producer.send('registered_topic',
                  value=bytes(json.dumps(user), encoding='utf-8'))

print('Pushed test events')

producer.flush()
