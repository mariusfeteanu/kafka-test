FROM debian:buster

# Setup java and check
RUN apt-get update -y
RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Needed tools and packages
RUN apt-get install -y wget

# Run zookeeper setup
COPY build/zookeeper.sh build/
RUN chmod +x build/zookeeper.sh && \
    build/zookeeper.sh

COPY entrypoint/zookeeper.sh entrypoint/
RUN chmod +x entrypoint/zookeeper.sh

ENTRYPOINT entrypoint/zookeeper.sh
