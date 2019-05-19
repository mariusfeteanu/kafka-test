from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

print('Pushing test events')

for k in range(2):
    producer.send('test_topic',
                  key=bytes(str(k), encoding='utf-8'),
                  value=b'yes there are bytes here')

for k in range(3):
    producer.send('test_topic',
                  key=bytes(str(k), encoding='utf-8'),
                  value=b'what is the problem')

for k in range(5):
    producer.send('test_topic',
                  key=bytes(str(k), encoding='utf-8'),
                  value=b'so how does this work')

producer.flush()
