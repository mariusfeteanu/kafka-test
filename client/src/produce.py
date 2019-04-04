from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

print('Pushing test events')

for k in range(10):
    producer.send('test_topic',
                  key=bytes(str(k), encoding='utf-8'),
                  value=b'yes there are bytes here')

producer.flush()
