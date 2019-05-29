import uuid

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

print('Pushing test events')

events = ['Hello there',
          'Does this work',
          'Putting the word the in here']

for event in events:
    for ii in range(5):
        producer.send('test_topic',
                      key=bytes(str(uuid.uuid1()), encoding='utf-8'),
                      value=bytes(event, encoding='utf-8'))

print('Pushed test events')

producer.flush()
