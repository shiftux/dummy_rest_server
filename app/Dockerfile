# NOTE: file needs to be built with the context in the repo root
FROM public.ecr.aws/lts/ubuntu:latest

RUN apt update -y && \
  apt install -y python3-pip python3-dev

ADD app/rest_routes.py /
ADD app/text_replies.py /

ENV RUNNING_IN_DOCKER=yes

EXPOSE 5000

RUN pip install Flask
RUN pip install json_logging

CMD ["python3", "-u", "/rest_routes.py"]