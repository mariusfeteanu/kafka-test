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

# Setup entrypoint
COPY entrypoint/zookeeper.sh entrypoint/
RUN chmod +x entrypoint/zookeeper.sh

# Add user
RUN useradd -ms /bin/bash zk
RUN chown zk:zk /var/lib/zookeeper
USER zk
WORKDIR /home/zk

ENTRYPOINT /entrypoint/zookeeper.sh
