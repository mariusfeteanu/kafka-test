FROM python:3.7-slim

RUN apt-get update -y
# no idea what this next line does
RUN mkdir -p /usr/share/man/man1
RUN apt-get install -y openjdk-8-jdk

RUN apt-get install -y wget telnet iputils-ping

RUN pip install pipenv

# Add user
RUN useradd -ms /bin/bash py

RUN mkdir -p /home/py/client/src && \
    chown py:py -R /home/py/client

WORKDIR /home/py/client

COPY --chown=py:py client/Pipfile client/Pipfile.lock client/client.sh ./
RUN chmod +x client.sh

USER py

RUN pipenv sync

ENTRYPOINT ./client.sh
