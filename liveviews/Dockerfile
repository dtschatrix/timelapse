FROM ubuntu:latest
WORKDIR /api
RUN apt update && apt upgrade -y

ENV DEBIAN_FRONTEND=noninteractive

RUN apt install -y build-essential python3-pip python3-dev ffmpeg

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "liveviews/__main__.py" ]