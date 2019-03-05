#!/usr/bin/env python3

from kafka import KafkaProducer

topic = 'test_topic'

producer = KafkaProducer(bootstrap_servers=['kafka1:9092'])

print('sending mssage')
future = producer.send(topic, b'the messagest')
