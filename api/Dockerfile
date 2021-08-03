FROM ubuntu:latest
EXPOSE 1337

RUN apt update && apt upgrade -y

RUN apt install -y build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel

COPY requirements.txt api/app/requirements.txt
RUN pip3 install -r api/app/requirements.txt

COPY app/ /api/app

#ENTRYPOINT [ "python3", "api/app/__main__.py" ]