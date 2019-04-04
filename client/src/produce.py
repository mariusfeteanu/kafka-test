from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

print('Pushing test events')

producer.send('ma_topic', b'yes there are bytes here')
