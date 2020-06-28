FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y build-essential

RUN mkdir -p /feedback-collection-system
WORKDIR /feedback-collection-system

COPY ./server.py .
COPY ./requirements.txt .
COPY ./Makefile .
COPY ./src ./src
COPY ./views ./views

RUN make install-requirements
RUN make prepare

EXPOSE 8080

CMD ["make", "run"]