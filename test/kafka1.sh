/usr/local/kafka/bin/kafka-console-producer.sh --broker-list kafka1:9092 --topic test

/usr/local/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka1:9092 --topic test --from-beginning

