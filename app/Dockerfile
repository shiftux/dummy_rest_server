# NOTE: file needs to be built with the context in the repo root
FROM ubuntu:20.10

RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev

ADD app/rest_routes.py /
ADD app/text_replies.py /

EXPOSE 5000

RUN pip install Flask
RUN pip install json_logging

CMD ["python3", "/rest_routes.py"]