FROM python:3.7-slim

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
