# NOTE: file needs to be built with the context in the repo root
FROM ubuntu:20.10

RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev

ADD app/rest_routes.py /
ADD app/text_replies.py /

ENV RUNNING_IN_DOCKER=yes

EXPOSE 5000

RUN pip install Flask
RUN pip install json_logging
RUN pip install google-python-cloud-debugger

CMD ["python3", "-u", "/rest_routes.py"]