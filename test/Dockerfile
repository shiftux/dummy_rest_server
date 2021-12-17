FROM ubuntu:20.10

RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev

ENV RUNNING_IN_DOCKER yes

ADD test_api.py /

RUN pip install pytest requests

CMD ["pytest", "/test_api.py"]