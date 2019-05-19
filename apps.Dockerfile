FROM debian:stretch

# Setup java and check
RUN apt-get update -y
RUN apt-get install -y openjdk-8-jdk

RUN apt-get install -y openjdk-8-jdk

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Needed tools and packages
RUN apt-get install -y wget telnet

# Setup entrypoint
COPY entrypoint/apps.sh entrypoint/
RUN chmod +x entrypoint/apps.sh

# Add user
RUN useradd -ms /bin/bash app

USER app
WORKDIR /home/app

COPY apps/word_count/target/scala-2.12/app-word-count-assembly-1.0.jar .

ENTRYPOINT ["/bin/bash", "/entrypoint/apps.sh"]
