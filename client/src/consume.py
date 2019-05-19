from kafka import KafkaConsumer

consumer_test_topic_wordcount = KafkaConsumer(
    'wordcount_test_topic',
    bootstrap_servers='kafka1:9092',
    auto_offset_reset='earliest')

print('Getting test events')

for message in consumer_test_topic_wordcount:
    print(f'{message.key} => {message.value}')
