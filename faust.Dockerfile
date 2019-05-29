FROM python:3.7-slim

RUN apt-get update -y
RUN apt-get install -y wget telnet iputils-ping

# Add user
RUN useradd -ms /bin/bash faust

WORKDIR /home/faust

COPY --chown=faust:faust ./faust/requirements.txt ./faust/run.sh ./
RUN chmod +x run.sh

RUN pip install -r requirements.txt

USER faust

ENTRYPOINT ["/bin/bash", "/home/faust/run.sh"]
