FROM debian:buster

# Setup java and check
RUN apt-get update -y
RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Needed tools and packages
RUN apt-get install -y wget telnet

# Run zookeeper setup
COPY build/kafka.sh build/
RUN chmod +x build/kafka.sh && \
    build/kafka.sh

# Setup entrypoint
COPY entrypoint/kafka.sh entrypoint/
RUN chmod +x entrypoint/kafka.sh

# Add user
RUN useradd -ms /bin/bash kafka
RUN chown kafka:kafka /tmp/kafka-logs
RUN mkdir -p /var/log/kafka && \
    chown kafka:kafka /var/log/kafka
USER kafka
WORKDIR /home/kafka

# These are the application logs for kafka
# not the data log (stored messages)
ENV LOG_DIR /var/log/kafka
ENTRYPOINT /entrypoint/kafka.sh
