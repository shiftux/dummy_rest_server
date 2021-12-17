FROM ubuntu:20.10

RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev

ADD rest_routes.py /
ADD text_replies.py /

EXPOSE 5000

RUN pip install Flask

CMD ["python3", "/rest_routes.py"]