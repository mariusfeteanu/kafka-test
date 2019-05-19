FROM debian:stretch

# Setup java and check
RUN apt-get update -y
RUN apt-get install -y openjdk-8-jdk

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

# Data logs
RUN mkdir -p /tmp/kafka-logs && \
    chown kafka:kafka /tmp/kafka-logs

# Application logs
RUN mkdir -p /var/log/kafka && \
    chown kafka:kafka /var/log/kafka
ENV LOG_DIR /var/log/kafka

USER kafka
WORKDIR /home/kafka

ENTRYPOINT /entrypoint/kafka.sh
