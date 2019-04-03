FROM debian:buster

# Setup java and check
RUN apt-get update -y
RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Needed tools and packages
RUN apt-get install -y wget telnet

# Setup entrypoint
COPY entrypoint/app_print.sh entrypoint/
RUN chmod +x entrypoint/app_print.sh

# Add user
RUN useradd -ms /bin/bash app

USER app
WORKDIR /home/app

COPY app_print/target/scala-2.12/app-print-assembly-1.0.jar .

ENTRYPOINT /entrypoint/app_print.sh
